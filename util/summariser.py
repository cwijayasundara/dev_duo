from dotenv import load_dotenv
from langchain.chains import load_summarize_chain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama

load_dotenv()

llm = Ollama(model="mixtral:instruct", temperature=0)

# llm = ChatOpenAI(temperature=0,
#                  model_name="gpt-4-0125-preview")

chain = load_summarize_chain(llm,
                             chain_type="map_reduce")

map_prompt_template = """
                      Write a summary of this chunk of text that includes the main points and any important details.
                      {text}
                      """

map_prompt = PromptTemplate(template=map_prompt_template, input_variables=["text"])

combine_prompt_template = """
                      Write a concise summary of the following text delimited by triple backquotes.
                      Return your response in bullet points which covers the key points of the text.
                      ```{text}```
                      BULLET POINT SUMMARY:
                      """

combine_prompt = PromptTemplate(
    template=combine_prompt_template, input_variables=["text"]
)

map_reduce_chain = load_summarize_chain(
    llm,
    chain_type="map_reduce",
    map_prompt=map_prompt,
    combine_prompt=combine_prompt,
    return_intermediate_steps=True,
)


def produce_summary(text):
    return map_reduce_chain.invoke(text)
