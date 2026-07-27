import streamlit as st

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/vinishaapr33/HCT-demo/main/olivia.jpg");
    background-size: cover;
}

/* Transparent box centered and moved down */
.text-box {
    background-color: rgba(255, 255, 255, 0.7);
    padding: 20px;
    border-radius: 10px;
    width: 60%;              /* box width */
    margin: 150px auto 0;    /* 👈 pushes down 150px, auto centers horizontally */
    text-align: center;      /* centers text inside */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Example text wrapped in the box
st.markdown('<div class="text-box">✨ Olivia in my first app ✨</div>', unsafe_allow_html=True)

from transformers import pipeline

st.title("Sentiment Analyzer")

user_text = st.text_input("Enter text:")
if st.button("Analyze"):
    sentiment = pipeline("sentiment-analysis")
    result = sentiment(user_text)[0]
    st.write("Label:", result['label'])
    st.write("Confidence:", result['score'])
    
