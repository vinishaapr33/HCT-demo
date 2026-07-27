import streamlit as st

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/vinishaapr33/HCT-demo/main/olivia.jpg");
    background-size: cover;
}

/* Big transparent overlay box */
.big-box {
    background-color: rgba(255, 255, 255, 0.15);  /* very light transparency */
    padding: 40px;
    border-radius: 15px;
    margin: 80px auto;
    width: 90%;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    display: flex;               /* 👈 arrange children in a row */
    justify-content: space-around; /* 👈 evenly space icons */
    align-items: center;
}

/* Icon boxes */
.icon-box {
    background-color: rgba(255, 255, 255, 0.7);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.25);
    text-align: center;
    font-size: 40px;   /* big icons */
    transition: all 0.3s ease;
}
.icon-box:hover {
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
    transform: scale(1.1);
    background-color: rgba(255, 255, 255, 0.85);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Big box with icons in a row
st.markdown("""
<div class="big-box">
    <div class="icon-box">🎵</div>
    <div class="icon-box">💻</div>
    <div class="icon-box">🌸</div>
    <div class="icon-box">✨</div>
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
    
