import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader

load_dotenv()

def load_document(saved_path):
    if saved_path.endswith(".pdf"):
        loader = PyPDFLoader(saved_path)
    elif saved_path.endswith(".docx"):
        loader = Docx2txtLoader(saved_path)
    else:
        st.error("Please upload PDF or DOCX only.")
        return ""
    documents = loader.load()
    return " ".join([doc.page_content for doc in documents])

st.title("📑 PDF/DOCX Summarizer")

uploaded_file = st.file_uploader("Upload a PDF or DOCX", type=["pdf", "docx"])

if uploaded_file:
    # Save file properly to disk
    saved_path = os.path.join("temp_" + uploaded_file.name)
    with open(saved_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = load_document(saved_path)
    if text:
        st.subheader("Extracted Content (first 500 chars):")
        st.write(text[:500] + "...")

        llm = ChatGroq(model="llama-3.3-70b-versatile")
        prompt = PromptTemplate(
            input_variables=["content"],
            template="Summarize the following document into clear bullet points:\n\n{content}\n\nSummary:"
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        summary = chain.invoke({"content": text})["text"]

        st.subheader("📌 Summary")
        st.write(summary)
