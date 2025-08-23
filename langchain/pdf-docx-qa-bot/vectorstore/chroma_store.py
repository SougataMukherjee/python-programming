from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_store(docs, persist_dir="chroma_db"):
    # Use HuggingFace embeddings (free + no API key required)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(docs, embeddings, persist_directory=persist_dir)
    return vectorstore
