from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import llm
from utils import map_sentiment_to_category

prompt_template = """
You are a sentiment analyzer.
Classify the following feedback into one of these categories:
- Happy
- Moderate
- OkOk
- Bad

Feedback: "{feedback}"
Answer with only one word from the categories.
"""

prompt = PromptTemplate(input_variables=["feedback"], template=prompt_template)

chain = LLMChain(llm=llm, prompt=prompt)

def analyze_sentiment(feedback: str) -> str:
    raw_output = chain.run(feedback)
    return map_sentiment_to_category(raw_output)
