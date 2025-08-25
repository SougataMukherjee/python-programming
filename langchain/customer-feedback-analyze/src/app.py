import streamlit as st
from utils import load_csv
from sentiment_chain import analyze_sentiment

st.title("📊 Customer Feedback Analyzer")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = load_csv(uploaded_file)
    st.write("### Uploaded Data")
    st.dataframe(df)

    if st.button("Analyze Sentiment"):
        df["Sentiment"] = df["feedback"].apply(analyze_sentiment)
        st.write("### Results")
        st.dataframe(df)
