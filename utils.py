import streamlit as st

def inject_custom_css():
    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');

    /* Global Font */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    /* Base theme adjustments */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 1200px;
    }

    /* Soft Gradient App Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #e2e8f0;
    }

    /* Hero Section */
    .hero-section {
        text-align: center;
        padding: 3rem 1rem;
        margin-bottom: 3rem;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

    /* Glowing Title */
    .glowing-title {
        font-family: 'Outfit', sans-serif;
        font-size: 5rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.5rem;
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px rgba(79, 172, 254, 0.5);
        line-height: 1.2;
    }

    /* Subtitle */
    .subtitle {
        font-size: 1.6rem;
        font-weight: 600;
        color: #a5b4fc;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    /* Hero Description */
    .hero-desc {
        font-size: 1.1rem;
        color: #94a3b8;
        max-width: 700px;
        margin: 0 auto;
        font-weight: 300;
        line-height: 1.6;
    }

    /* Glassmorphism styling for output box and containers */
    .glass-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
        min-height: 150px;
        margin-top: 10px;
        margin-bottom: 10px;
        font-size: 1.1rem;
        color: #f8fafc;
    }

    .glass-box:hover {
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }

    /* Styling for generic stTextAreas */
    div[data-baseweb="textarea"] > div {
        border-radius: 12px !important;
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transition: all 0.3s ease;
    }

    div[data-baseweb="textarea"] textarea {
        color: #f8fafc !important;
    }

    div[data-baseweb="textarea"] > div:focus-within {
        border-color: #4facfe !important;
        box-shadow: 0 0 15px rgba(79, 172, 254, 0.3) !important;
    }

    /* Button styling overrides */
    div[data-testid="stButton"] button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.1);
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 0.5rem 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    div[data-testid="stButton"] button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(79, 172, 254, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: white;
    }

    div[data-testid="stButton"] button:active {
        transform: translateY(1px);
    }

    /* Character count text */
    .char-count {
        font-size: 0.85rem;
        color: #64748b;
        text-align: right;
        margin-top: 8px;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .animated {
        animation: fadeIn 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }

    /* Sidebar and Heading overrides */
    h3, h2, h1 {
        color: #e2e8f0 !important;
        font-family: 'Outfit', sans-serif !important;
    }
    
    /* Custom cards for analytics and detection */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    }
    .metric-card h2 {
        margin: 0;
        font-size: 2.5rem;
        background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .metric-card p {
        margin: 5px 0 0 0;
        color: #94a3b8;
        font-size: 1.1rem;
    }

    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
