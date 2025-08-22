from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq   
import os

# Load env variables
load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)  
print("API Key loaded?", os.getenv("GROQ_API_KEY") is not None)

# Initialize chat history
chat_history = []

# user message 
message = [
    SystemMessage(content="Solve the following math problem"),
    HumanMessage(content="what is 100 divide by 5?")
]
result = model.invoke(message)
print(f"answer from AI: {result.content}")

# ai message 
message = [
    SystemMessage(content="Solve the following math problem"),
    HumanMessage(content="what is 100 divide by 5?"),
    AIMessage(content="81 divide by 9 is 9"),
    HumanMessage(content="what is 10 times 5?")
]
result = model.invoke(message)
print(f"answer from AI: {result.content}")

# add system role
system_message = SystemMessage(content="you are a helpful AI assistant")
chat_history.append(system_message)

# chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    print(f"AI: {response}")

print("-------message history------")
print(chat_history)
