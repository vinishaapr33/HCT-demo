
import streamlit as st
from transformers import pipeline

# Background + styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/vinishaapr33/HCT-demo/main/olivia.jpg");
    background-size: cover;
}

/* Big transparent overlay */
.big-box {
    background-color: rgba(255, 255, 255, 0.15);
    padding: 50px;
    border-radius: 20px;
    margin: 100px auto;
    width: 80%;
    box-shadow: 0px 4px 25px rgba(0,0,0,0.3);
    text-align: center;
}

/* Highlight box */
.sentiment-box {
    background-color: rgba(255, 215, 0, 0.8);
    padding: 40px;
    border-radius: 15px;
    box-shadow: 0px 6px 30px rgba(255, 215, 0, 0.6);
    transition: all 0.3s ease;
}
.sentiment-box:hover {
    transform: scale(1.05);
    background-color: rgba(255, 215, 0, 0.95);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Your actual app code inside the styled structure
st.markdown('<div class="big-box"><div class="sentiment-box"></div></div>', unsafe_allow_html=True)

st.title("Sentiment Analyzer")

user_text = st.text_input("Enter text:")
if st.button("Analyze"):
    sentiment = pipeline("sentiment-analysis")
    result = sentiment(user_text)[0]
    st.write("Label:", result['label'])
    st.write("Confidence:", result['score'])
