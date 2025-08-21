from langchain.chains import RetrievalQA
from models.llm_setup import load_llm

def get_qa_chain(vectorstore):
    llm = load_llm()
    retriever = vectorstore.as_retriever()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
