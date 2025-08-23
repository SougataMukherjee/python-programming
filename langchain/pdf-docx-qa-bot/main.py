from loaders.doc_loader import load_documents
from vectorstore.chroma_store import create_vector_store
from qa.qa_chain import create_qa_chain

def main():
    # Load your document
    docs = load_documents("data/sample.pdf")

    # Create vector store
    vectorstore = create_vector_store(docs)

    # Create QA chain
    qa_chain = create_qa_chain(vectorstore)

    print("Ask a question about your document:")
    while True:
        query = input(">>> ")
        if query.lower() in ["exit", "quit"]:
            break
        response = qa_chain({"query": query})
        print("Answer:", response["result"])

if __name__ == "__main__":
    main()
