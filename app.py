import streamlit as st
from transformers import pipeline

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="✨",
    layout="centered"
)

# ---------------- LOAD MODEL ---------------- #

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

sentiment_pipeline = load_model()

# ---------------- CSS ---------------- #

st.markdown("""
<style>

/* ---------------- BACKGROUND ---------------- */

[data-testid="stAppViewContainer"]{
    background-image:url("https://raw.githubusercontent.com/vinishaapr33/HCT-demo/main/olivia.jpg");
    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    background-attachment:fixed;
}

/* Remove Streamlit header */

[data-testid="stHeader"]{
    background:transparent;
}

[data-testid="stToolbar"]{
    background:transparent;
}

/* ---------------- MAIN GLASS PANEL ---------------- */

.block-container{

    max-width:820px !important;

    margin:auto !important;

    margin-top:60px !important;

    padding:45px !important;

    background:rgba(255,255,255,0.09);

    backdrop-filter:blur(18px);
    -webkit-backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,0.28);

    border-radius:24px;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.28),
        0 0 15px rgba(255,255,255,0.08);

}

/* ---------------- REMOVE WHITE BACKGROUNDS ---------------- */

div[data-testid="element-container"],
div[data-testid="stVerticalBlock"],
div[data-testid="stHorizontalBlock"],
div[data-testid="stMarkdownContainer"],
section{
    background:transparent !important;
}

/* ---------------- TEXT ---------------- */

h1{

    color:white !important;

    text-align:center;

    font-size:44px;

    text-shadow:0 0 4px rgba(255,255,255,0.30);

}

h2,h3,h4,h5,h6,
label,
p,
span,
div{

    color:white !important;

    text-shadow:0 0 1px rgba(255,255,255,0.15);

}

/* ---------------- INPUT BOX ---------------- */

.stTextInput input{

    background:rgba(255,255,255,0.14)!important;

    color:black!important;

    border:1px solid rgba(255,255,255,0.30)!important;

    border-radius:14px!important;

    backdrop-filter:blur(12px);

    padding:12px;

}

/* Placeholder */

.stTextInput input::placeholder{

    color:rgba(255,255,255,0.75)!important;

}

/* ---------------- BUTTON ---------------- */

.stButton > button{

    width:100%;

    background:rgba(255,255,255,0.12);

    color:white;

    border:1px solid rgba(255,255,255,0.28);

    border-radius:14px;

    backdrop-filter:blur(10px);

    transition:0.3s;

}

.stButton > button:hover{

    background:rgba(255,255,255,0.20);

    box-shadow:0 0 15px rgba(255,255,255,0.20);

}

/* ---------------- RESULT BOX ---------------- */

div[data-testid="stAlert"]{

    background:rgba(255,255,255,0.10)!important;

    border:1px solid rgba(255,255,255,0.20)!important;

    color:white!important;

    backdrop-filter:blur(10px);

}

/* Success messages */

div[data-testid="stSuccess"]{

    background:rgba(255,255,255,0.08)!important;

}

/* Warning */

div[data-testid="stWarning"]{

    background:rgba(255,255,255,0.08)!important;

}

</style>
""", unsafe_allow_html=True)
# ---------------- APP ---------------- #

st.markdown("<br>", unsafe_allow_html=True)

st.title("✨ Sentiment Analyzer")

st.markdown(
    "<p style='text-align:center; font-size:18px;'>"
    "Analyze the sentiment of any sentence using AI."
    "</p>",
    unsafe_allow_html=True,
)

st.write("")

user_text = st.text_input(
    "Enter your text",
    placeholder="Type something here..."
)

st.write("")

if st.button("🔍 Analyze"):

    if user_text.strip():

        with st.spinner("Analyzing..."):

            result = sentiment_pipeline(user_text)[0]

        st.success("Analysis Complete")

      if result["label"] == "POSITIVE":
    st.success(f"😊 Positive ({result['score']:.2%})")
else:
    st.error(f"😞 Negative ({result['score']:.2%})")

    else:

        st.warning("Please enter some text before clicking Analyze.")
