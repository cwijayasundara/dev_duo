from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama

load_dotenv()

# llm = ChatOpenAI(temperature=0,
#                  model_name="gpt-4-0125-preview")

llm = Ollama(model="mixtral:instruct", temperature=0)

template = """

You are an expert in text formatting.

Format the provided text {text} in a way that it is easy to read and understand in point form.

some examples of point form are:

- This is the first point
- This is the second point

input text: {text}
"""

prompt = PromptTemplate.from_template(template)

llm_chain = LLMChain(prompt=prompt, llm=llm)


def format_text(text):
    return llm_chain.run(text)
