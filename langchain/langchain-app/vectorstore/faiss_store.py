from langchain_community.vectorstores import FAISS
from models.llm_setup import load_embeddings

def create_vectorstore(docs):
    embeddings = load_embeddings()
    return FAISS.from_documents(docs, embeddings)
