import streamlit as st
from utils import inject_custom_css
import time

st.set_page_config(
    page_title="Tone Conversion - Mirai",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_custom_css()

st.markdown("<h2 style='text-align: center; color: #4facfe;'>AI Tone Conversion</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8; margin-bottom: 2rem;'>Convert translated text into different tones or styles.</p>", unsafe_allow_html=True)

# Note about mock implementation
st.info("Note: Tone Conversion currently relies on a simulated AI logic for demonstration purposes. Connecting a generative LLM (like OpenAI/Gemini) will provide real conversational rewriting.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Original Text")
    input_text = st.text_area("Enter your text here:", height=200, key="tone_input")
    
    tone = st.selectbox(
        "Select Target Tone",
        ["Formal", "Casual", "Professional", "Friendly", "Academic"]
    )
    
    convert_btn = st.button("🎭 Convert Tone", use_container_width=True)

with col2:
    st.markdown("### Converted Text")
    
    if convert_btn:
        if not input_text.strip():
            st.error("Please enter some text to convert.")
        else:
            with st.spinner(f"Converting to {tone} tone..."):
                time.sleep(1.5) # Simulate API call
                
                # Mock tone conversion logic
                converted_text = input_text
                if tone == "Formal":
                    converted_text = f"Dear Sir/Madam,\n\nRegarding the matter: {input_text}\n\nYours faithfully."
                elif tone == "Casual":
                    converted_text = f"Hey! So basically, {input_text.lower()} 🚀"
                elif tone == "Professional":
                    converted_text = f"As per our discussion, {input_text}. Please advise on the next steps."
                elif tone == "Friendly":
                    converted_text = f"Hi there! 😊 Just wanted to share: {input_text}. Hope you have a great day!"
                elif tone == "Academic":
                    converted_text = f"It is hypothesized that {input_text}. Further research is required to substantiate this claim."

                st.markdown(f"<div class='glass-box animated'>{converted_text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='glass-box' style='color: #64748b; font-style: italic;'>Converted text will appear here...</div>", unsafe_allow_html=True)
