import streamlit as st
from transformers import pipeline

# Load Hugging Face sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

# Background + styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/vinishaapr33/HCT-demo/main/olivia.jpg");
    background-size: cover;
}

/* Big transparent overlay wrapping all content */
.big-box {
    background-color: rgba(255, 255, 255, 0.15);  /* 👈 adjust opacity */
    padding: 50px;
    border-radius: 20px;
    margin: 60px auto;
    width: 85%;
    border: 2px solid rgba(255,255,255,0.6);      /* subtle white border */
    box-shadow: 0px 0px 20px rgba(255,255,255,0.7); /* glowy aura */
    color: white;                                 /* 👈 makes text white */
    text-shadow: 0px 0px 8px rgba(255,255,255,0.8); /* 👈 glow effect */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Wrap ALL app content inside the big transparent box
st.markdown('<div class="big-box">', unsafe_allow_html=True)

# Actual app code
st.title("Sentiment Analyzer")
user_text = st.text_input("Enter text:")
if st.button("Analyze"):
    sentiment = pipeline("sentiment-analysis")
    result = sentiment(user_text)[0]
    st.write("Label:", result['label'])
    st.write("Confidence:", result['score'])

st.markdown('</div>', unsafe_allow_html=True)
