from langchain_groq import ChatGroq
from config import GROQ_API_KEY

def get_groq_llm():
    return ChatGroq(
        api_key=GROQ_API_KEY,
        model_name="qwen/qwen3-32b", 
        temperature=0.7  
    )
