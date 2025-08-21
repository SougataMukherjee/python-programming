from langchain_openai import OpenAIEmbeddings, ChatOpenAI

def load_llm():
    return ChatOpenAI(model="gpt-3.5-turbo")

def load_embeddings():
    return OpenAIEmbeddings()
