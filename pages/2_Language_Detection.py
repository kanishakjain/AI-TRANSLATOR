import streamlit as st
from langdetect import detect_langs
import langdetect
from utils import inject_custom_css

st.set_page_config(
    page_title="Detection - Mirai",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded"
)

inject_custom_css()

# Supported human-readable mapping
LANGUAGE_MAPPING = {
    "en": "English", "hi": "Hindi", "fr": "French", "de": "German", 
    "es": "Spanish", "ja": "Japanese", "ko": "Korean", "zh-cn": "Chinese", 
    "ru": "Russian", "ar": "Arabic", "it": "Italian", "pt": "Portuguese",
    "nl": "Dutch", "tr": "Turkish", "pl": "Polish", "sv": "Swedish"
}

st.markdown("<h2 style='text-align: center; color: #4facfe;'>Language Detection</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; margin-bottom: 2rem;'>Instantly identify the language of your text with high accuracy.</p>", unsafe_allow_html=True)

input_text = st.text_area("Enter text to detect language:", height=200, key="detect_input")

if st.button("🔍 Detect Language", use_container_width=True):
    if not input_text.strip():
        st.error("Please enter some text.")
    else:
        with st.spinner("Analyzing text..."):
            try:
                # Get a list of detected languages with probabilities
                langs = detect_langs(input_text)
                top_lang = langs[0]
                lang_code = top_lang.lang
                confidence = top_lang.prob * 100
                
                lang_name = LANGUAGE_MAPPING.get(lang_code, lang_code.upper())
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"""
                <div class="metric-card animated">
                    <p>Detected Language</p>
                    <h2>{lang_name}</h2>
                    <p style="margin-top: 15px;">Confidence: <strong>{confidence:.1f}%</strong></p>
                </div>
                """, unsafe_allow_html=True)
                
                # Show breakdown if there are multiple possibilities
                if len(langs) > 1:
                    st.markdown("### Other Possibilities")
                    for l in langs[1:]:
                        st.write(f"- **{LANGUAGE_MAPPING.get(l.lang, l.lang.upper())}**: {l.prob*100:.1f}%")
                        
            except langdetect.lang_detect_exception.LangDetectException:
                st.error("Could not detect the language. The text might be too short or contains no words.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
