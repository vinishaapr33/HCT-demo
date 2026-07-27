import streamlit as st

import streamlit as st

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/vinishaapr33/HCT-demo/main/olivia.jpg");
    background-size: cover;
}

/* Big transparent overlay box */
.big-box {
    background-color: rgba(255, 255, 255, 0.2);
    padding: 40px;
    border-radius: 15px;
    margin: 50px auto;
    width: 80%;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

/* Smaller floating boxes */
.text-box {
    background-color: rgba(255, 255, 255, 0.7);
    padding: 20px;
    border-radius: 10px;
    margin: 20px 0;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.25);
    transition: all 0.3s ease;   /* 👈 smooth animation */
}

/* Hover effect */
.text-box:hover {
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);   /* stronger shadow */
    transform: scale(1.02);                     /* slight zoom */
    background-color: rgba(255, 255, 255, 0.85); /* glow by reducing transparency */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Big box wrapping everything
st.markdown("""
<div class="big-box">
    <div class="text-box">✨ Olivia in my first app ✨</div>
    <div class="text-box">Readable text with floating transparent boxes</div>
    <div class="text-box">Symmetric layout with overlay + shadows</div>
    <div class="text-box">Now with hover glow ✨</div>
</div>
""", unsafe_allow_html=True)


from transformers import pipeline

st.title("Sentiment Analyzer")

user_text = st.text_input("Enter text:")
if st.button("Analyze"):
    sentiment = pipeline("sentiment-analysis")
    result = sentiment(user_text)[0]
    st.write("Label:", result['label'])
    st.write("Confidence:", result['score'])
    
