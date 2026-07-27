import streamlit as st
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/vinishaapr33/HCT-demo/main/olivia.jpg");
    background-size: cover;
}
.block-container {
    background-color: rgba(255, 255, 255, 0.7);
    padding: 20px;
    border-radius: 10px;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("My Polished Hugging Face App ✨")
st.write("Readable text on top of background!")

from transformers import pipeline

st.title("Sentiment Analyzer")

user_text = st.text_input("Enter text:")
if st.button("Analyze"):
    sentiment = pipeline("sentiment-analysis")
    result = sentiment(user_text)[0]
    st.write("Label:", result['label'])
    st.write("Confidence:", result['score'])
    uploaded = st.file_uploader("olivia.jpg")
if uploaded:
    st.image(uploaded)
