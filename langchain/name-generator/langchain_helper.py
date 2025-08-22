from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.agents import initialize_agent, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_experimental.tools import PythonREPLTool


import os

# Load .env file
load_dotenv()

def generate_name(sp_type, food_type):
    # Fetch the API key from environment
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("⚠️ GROQ_API_KEY is not set. Please check your .env file.")

    prompt_template_name = PromptTemplate(
        input_variables=['sp_type', 'food_type'],
        template="I am a {sp_type}. I want a cool name for me. I love to eat {food_type}."
    )

    # Pass API key explicitly
    llm = ChatGroq(model="llama3-8b-8192", api_key=groq_api_key)

    # Build chain
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    
    response = name_chain.invoke({'sp_type': sp_type, 'food_type': food_type})
    return response["text"] 




def langchain_agent():
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("⚠️ GROQ_API_KEY is not set. Please check your .env file.")

    llm = ChatGroq(model="llama3-8b-8192", api_key=groq_api_key)

    # Load wikipedia from community tools
    wiki_tools = load_tools(["wikipedia"], llm=llm)

    # Add python repl manually
    python_repl = PythonREPLTool()
    tools = wiki_tools + [python_repl]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    result = agent.run("What is the average age of the cat? Use wikipedia if needed and calculate with python.")
    print(result)



if __name__ == "__main__":
    print(generate_name('cat', 'milk'))
    # langchain_agent()
