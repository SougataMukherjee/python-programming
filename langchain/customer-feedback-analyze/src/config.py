import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load your GROQ API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama3-8b-8192"
)
