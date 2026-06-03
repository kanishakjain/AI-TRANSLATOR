import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect
import langdetect
import pyperclip
import PyPDF2
import docx
from utils import inject_custom_css

st.set_page_config(
    page_title="Translator - Mirai",
    page_icon="🗣️",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_custom_css()

# --- SUPPORTED LANGUAGES ---
LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar"
}

TARGET_LANGUAGES = {k: v for k, v in LANGUAGES.items() if k != "Auto Detect"}

# --- SESSION STATE INITIALIZATION ---
if 'history' not in st.session_state:
    st.session_state.history = []
if 'source_lang' not in st.session_state:
    st.session_state.source_lang = "Auto Detect"
if 'target_lang' not in st.session_state:
    st.session_state.target_lang = "English"
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""
if 'translated_text' not in st.session_state:
    st.session_state.translated_text = ""

# --- SIDEBAR (History) ---
with st.sidebar:
    st.markdown("### 🕒 Translation History")
    if st.button("Clear History", use_container_width=True):
        st.session_state.history = []
        st.rerun()
    
    st.divider()
    
    if not st.session_state.history:
        st.info("No history yet.")
    else:
        for idx, item in enumerate(reversed(st.session_state.history)):
            st.markdown(f"**{item['source']} ➔ {item['target']}**")
            st.caption(f"Input: {item['input'][:50]}...")
            st.caption(f"Output: {item['output'][:50]}...")
            st.divider()

st.markdown("<h2 style='text-align: center; color: #4facfe;'>TranslateX Translator</h2>", unsafe_allow_html=True)

# Top controls: Language Selection and Swap Button
col1, col2, col3 = st.columns([4, 1, 4])

with col1:
    source_lang_name = st.selectbox(
        "Source Language",
        options=list(LANGUAGES.keys()),
        index=list(LANGUAGES.keys()).index(st.session_state.source_lang),
        key="source_lang_select"
    )

with col2:
    st.write("")
    st.write("")
    if st.button("🔄 Swap", use_container_width=True, help="Swap source and target languages"):
        if source_lang_name != "Auto Detect":
            temp = source_lang_name
            st.session_state.source_lang = st.session_state.target_lang
            st.session_state.target_lang = temp
            st.rerun()
        else:
            st.warning("Cannot swap 'Auto Detect'.")

with col3:
    target_lang_name = st.selectbox(
        "Target Language",
        options=list(TARGET_LANGUAGES.keys()),
        index=list(TARGET_LANGUAGES.keys()).index(st.session_state.target_lang),
        key="target_lang_select"
    )

st.session_state.source_lang = source_lang_name
st.session_state.target_lang = target_lang_name

# Input and Output Layout
in_col, out_col = st.columns(2)

with in_col:
    st.markdown("### Document Upload")
    uploaded_file = st.file_uploader("Upload a file to extract text", type=["txt", "pdf", "docx"], label_visibility="collapsed")
    if uploaded_file is not None:
        with st.spinner("Extracting text..."):
            try:
                extracted_text = ""
                if uploaded_file.name.endswith(".txt"):
                    extracted_text = uploaded_file.read().decode("utf-8")
                elif uploaded_file.name.endswith(".pdf"):
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    for page in pdf_reader.pages:
                        extracted_text += page.extract_text() + "\n"
                elif uploaded_file.name.endswith(".docx"):
                    doc = docx.Document(uploaded_file)
                    for para in doc.paragraphs:
                        extracted_text += para.text + "\n"
                
                if extracted_text.strip():
                    if st.session_state.input_text != extracted_text.strip():
                        st.session_state.input_text = extracted_text.strip()
                        st.rerun()
                else:
                    st.warning("No text found in the uploaded file.")
            except Exception as e:
                st.error(f"Error extracting text: {e}")

    st.markdown("### Input Text")
    input_text = st.text_area(
        "Enter text here...",
        value=st.session_state.input_text,
        height=200,
        label_visibility="collapsed",
        key="text_input"
    )
    
    st.session_state.input_text = input_text
    st.markdown(f"<div class='char-count'>{len(input_text)} characters</div>", unsafe_allow_html=True)

    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        translate_clicked = st.button("🚀 Translate", use_container_width=True)
    with btn_col2:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.input_text = ""
            st.session_state.translated_text = ""
            st.rerun()

with out_col:
    st.markdown("### Translated Text")
    
    if translate_clicked:
        if not input_text.strip():
            st.error("Please enter some text to translate.")
        else:
            with st.spinner("Translating using AI..."):
                try:
                    detected_lang_code = LANGUAGES[source_lang_name]
                    actual_source_name = source_lang_name
                    
                    if source_lang_name == "Auto Detect":
                        try:
                            detected_lang_code = detect(input_text)
                            for name, code in TARGET_LANGUAGES.items():
                                if code == detected_lang_code:
                                    actual_source_name = name
                                    break
                            else:
                                actual_source_name = f"Detected ({detected_lang_code})"
                        except langdetect.lang_detect_exception.LangDetectException:
                            detected_lang_code = "auto"
                            actual_source_name = "Auto Detect"

                    target_code = TARGET_LANGUAGES[target_lang_name]
                    translator = GoogleTranslator(source=detected_lang_code, target=target_code)
                    translated = translator.translate(input_text)
                    
                    st.session_state.translated_text = translated
                    
                    st.session_state.history.append({
                        "source": actual_source_name,
                        "target": target_lang_name,
                        "input": input_text,
                        "output": translated
                    })
                    
                except Exception as e:
                    st.error(f"An error occurred during translation: {e}")

    output_text = st.session_state.translated_text
    st.markdown(f"<div class='glass-box animated'>{output_text if output_text else 'Translation will appear here...'}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='char-count'>{len(output_text)} characters</div>", unsafe_allow_html=True)

    if output_text:
        action_col1, action_col2 = st.columns(2)
        with action_col1:
            if st.button("📋 Copy", use_container_width=True, help="Requires clipboard access or local run"):
                try:
                    pyperclip.copy(output_text)
                    st.toast("Copied to clipboard!", icon="✅")
                except Exception as e:
                    st.error("Clipboard not supported in this environment.")
                    
        with action_col2:
            st.download_button(
                label="💾 Download TXT",
                data=output_text,
                file_name="translation.txt",
                mime="text/plain",
                use_container_width=True
            )
