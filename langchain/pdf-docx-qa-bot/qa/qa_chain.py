from langchain.chains import RetrievalQA
from llm.groq_llm import get_groq_llm

def create_qa_chain(vectorstore):
    llm = get_groq_llm()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain
