from langchain_community.document_loaders import TextLoader

def load_docs(file_path="data/docs.txt"):
    loader = TextLoader(file_path)
    return loader.load()
