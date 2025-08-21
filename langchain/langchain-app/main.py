from utils.loader import load_docs
from vectorstore.faiss_store import create_vectorstore
from chains.qa_chain import get_qa_chain
from dotenv import load_dotenv
import os

load_dotenv()
print("API Key loaded?", os.getenv("OPENAI_API_KEY") is not None)

def main():
    docs = load_docs("data/docs.txt")
    vs = create_vectorstore(docs)
    qa = get_qa_chain(vs)

    while True:
        query = input("Ask a question (q to quit): ")
        if query.lower() == "q":
            break
        answer = qa.run(query)
        print("Answer:", answer)

if __name__ == "__main__":
    main()
