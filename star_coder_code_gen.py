from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

llm = Ollama(model="starcoder2:15b")


def execute_star_coder_2(request):
    response = llm.invoke(request)
    return response
