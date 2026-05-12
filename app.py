import streamlit as st
from utils import inject_custom_css

st.set_page_config(
    page_title="Mirai | Every Voice Understood",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_custom_css()

# --- MAIN APP LAYOUT ---
st.markdown("""
<div class="hero-section animated">
    <div class="glowing-title">Mirai</div>
    <div class="subtitle">Every Voice Understood</div>
    <div class="hero-desc">A futuristic AI-powered multilingual translator focused on breaking language barriers through intelligent communication and document translation.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-box animated" style="text-align: center; animation-delay: 0.1s;">
        <h3 style="color: #4facfe !important;">🗣️ Translator</h3>
        <p style="color: #94a3b8;">Translate text and documents instantly between 10+ languages with auto-detection.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Translator", use_container_width=True, key="btn_trans"):
        st.switch_page("pages/1_Translator.py")
        
    st.markdown("""
    <div class="glass-box animated" style="text-align: center; animation-delay: 0.3s;">
        <h3 style="color: #4facfe !important;">🎭 AI Tone Conversion</h3>
        <p style="color: #94a3b8;">Change the tone of your text to Formal, Casual, Professional, and more.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Tone Conversion", use_container_width=True, key="btn_tone"):
        st.switch_page("pages/3_Tone_Conversion.py")

with col2:
    st.markdown("""
    <div class="glass-box animated" style="text-align: center; animation-delay: 0.2s;">
        <h3 style="color: #4facfe !important;">🔍 Language Detection</h3>
        <p style="color: #94a3b8;">Detect the language of any text instantly with high accuracy and confidence metrics.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Detection", use_container_width=True, key="btn_det"):
        st.switch_page("pages/2_Language_Detection.py")
        
    st.markdown("""
    <div class="glass-box animated" style="text-align: center; animation-delay: 0.4s;">
        <h3 style="color: #4facfe !important;">📊 Accuracy Analytics</h3>
        <p style="color: #94a3b8;">Visualize translation confidence and detected language accuracy through interactive charts.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Analytics", use_container_width=True, key="btn_acc"):
        st.switch_page("pages/4_Translation_Accuracy.py")
