import streamlit as st
from transformers import pipeline

# -------------------- Page Config --------------------
st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

# -------------------- Load Model --------------------
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

sentiment_pipeline = load_model()

# -------------------- CSS --------------------
st.markdown("""
<style>

/* Background image */
[data-testid="stAppViewContainer"]{
    background-image: url("https://raw.githubusercontent.com/vinishaapr33/HCT-demo/main/olivia.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;

    display: flex;
    justify-content: center;
    min-height: 100vh;
}

/* Main content box */
.main .block-container{
    text-align: center;
    margin-top: 250px;   /* 👈 move content downward */
    /* Try negative values (e.g., -100px) if you want it higher */
}

/* Title */
h1{
    color:white !important;
    text-shadow:0 0 10px white;
}

/* Labels and results */
label, p, span, div{
    color:white !important;
    text-shadow:0 0 8px rgba(255,255,255,0.9);
}

/* Text input */
.stTextInput input{
    background:rgba(255,255,255,0.7)!important;
    color:black!important;
    border:1px solid rgba(255,255,255,0.8)!important;
    border-radius:12px!important;
    padding:10px;
}

/* Placeholder */
.stTextInput input::placeholder{
    color:rgba(0,0,0,0.6)!important;
}

/* Button */
.stButton>button{
    width:100%;
    background:rgba(255,255,255,0.18);
    color:white;
    border:1px solid rgba(255,255,255,0.7);
    border-radius:12px;
    font-weight:bold;
    box-shadow:0 0 15px rgba(255,255,255,0.6);
}

.stButton>button:hover{
    background:rgba(255,255,255,0.3);
    color:white;
}

/* Alerts */
.stAlert{
    background:rgba(255,255,255,0.12)!important;
    color:white!important;
}

</style>
""", unsafe_allow_html=True)

# -------------------- App --------------------
st.title("✨ Sentiment Analyzer ✨")

user_text = st.text_input("Enter text")

if st.button("Analyze"):
    if user_text.strip():
        result = sentiment_pipeline(user_text)[0]
        st.write(f"### **Label:** {result['label']}")
        st.write(f"### **Confidence:** {result['score']:.2%}")
    else:
        st.warning("Please enter some text.")
