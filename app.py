import streamlit as st
from transformers import pipeline

# ---------------- Page Config ----------------

st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="✨",
    layout="centered"
)

# ---------------- Load Model ----------------

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

sentiment_pipeline = load_model()

# ---------------- CSS ----------------

st.markdown("""
<style>

/* Background */

[data-testid="stAppViewContainer"]{
    background-image:url("https://raw.githubusercontent.com/vinishaapr33/HCT-demo/main/olivia.jpg");
    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    background-attachment:fixed;
}

/* Remove Streamlit default backgrounds */

[data-testid="stHeader"],
[data-testid="stToolbar"]{
    background:transparent;
}

/* Main Glass Card */

.main .block-container{

    max-width:850px;

    margin:auto;
    margin-top:70px;

    padding:50px;

    border-radius:30px;

    background:rgba(255,255,255,.08);

    backdrop-filter:blur(20px);
    -webkit-backdrop-filter:blur(20px);

    border:1.5px solid rgba(255,255,255,.35);

    box-shadow:
        0 0 20px rgba(255,255,255,.18),
        0 8px 40px rgba(0,0,0,.30);

}

/* Make every Streamlit container transparent */

div[data-testid="stVerticalBlock"],
div[data-testid="stHorizontalBlock"],
div[data-testid="element-container"],
div[data-testid="stMarkdownContainer"],
section{
    background:transparent !important;
}

/* Headings */

h1,h2,h3,h4,h5,h6{

    color:white !important;

    text-align:center;

    text-shadow:
        0 0 8px white,
        0 0 18px white;
}

/* Text */

label,p,span,div{

    color:white !important;

    text-shadow:0 0 6px rgba(255,255,255,.9);
}

/* Input Box */

.stTextInput input{

    background:rgba(255,255,255,.10)!important;

    color:white!important;

    border:1px solid rgba(255,255,255,.45)!important;

    border-radius:15px!important;

    backdrop-filter:blur(10px);

    padding:12px;
}

/* Placeholder */

.stTextInput input::placeholder{

    color:rgba(255,255,255,.70)!important;
}

/* Button */

.stButton>button{

    width:100%;

    background:rgba(255,255,255,.10);

    color:white;

    border:1px solid rgba(255,255,255,.45);

    border-radius:15px;

    backdrop-filter:blur(10px);

    transition:.3s;

    box-shadow:0 0 18px rgba(255,255,255,.15);
}

.stButton>button:hover{

    background:rgba(255,255,255,.18);

    box-shadow:0 0 28px rgba(255,255,255,.35);

    transform:scale(1.02);
}

/* Alerts */

div[data-testid="stAlert"]{

    background:rgba(255,255,255,.08)!important;

    border:1px solid rgba(255,255,255,.25)!important;

    backdrop-filter:blur(10px);

    color:white!important;
}

/* Results */

div[data-testid="stText"]{
    background:transparent!important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- App ----------------

st.title("✨ Sentiment Analyzer")

st.write("Enter a sentence below to analyze its sentiment.")

user_text = st.text_input("Enter Text")

if st.button("Analyze"):

    if user_text.strip():

        result = sentiment_pipeline(user_text)[0]

        st.subheader("Result")

        st.write(f"**Label:** {result['label']}")

        st.write(f"**Confidence:** {result['score']:.2%}")

    else:

        st.warning("Please enter some text.")
