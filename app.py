import streamlit as st
import transformers import pipeline
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/vinishaapr33/HCT-demo/main/olivia.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Main content container */
[data-testid="stMainBlockContainer"] {
    background: rgba(255,255,255,0.12);
    border: 2px solid rgba(255,255,255,0.6);
    border-radius: 20px;
    padding: 40px;
    margin-top: 40px;
    margin-bottom: 40px;
    box-shadow: 0 0 20px rgba(255,255,255,0.7);
}

/* All text */
h1, h2, h3, h4, h5, h6, p, label, div, span {
    color: white !important;
    text-shadow: 0 0 8px rgba(255,255,255,0.9);
}

/* Text input */
.stTextInput input {
    background: rgba(255,255,255,0.12) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.5);
}

/* Placeholder */
.stTextInput input::placeholder {
    color: rgba(255,255,255,0.7);
}

/* Button */
.stButton > button {
    background: rgba(255,255,255,0.15);
    color: white;
    border: 1px solid white;
    box-shadow: 0 0 10px white;
}
</style>
st.title("Sentiment Analyzer")

user_text = st.text_input("Enter text:")

if st.button("Analyze"):
    result = sentiment_pipeline(user_text)[0]
    st.write("Label:", result["label"])
    st.write("Confidence:", f"{result['score']:.2f}")
