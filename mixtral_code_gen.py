from langchain_community.llms import Ollama
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = Ollama(model="mixtral:instruct")

prompt_str = """

System : 

You are an expert Python engineer with Deep Neural Network (DNN) Tensorflow,  Keras and PyTorch 
knowledge and also Python microservice knowledge. 

Generate fully functional and fully working code in Python for the provided scenario. 

provided scenario. {input}

Do not generate any other instructions and just code!

"""

prompt = ChatPromptTemplate.from_template(prompt_str)

output_parser = StrOutputParser()

chain = (
        {"input": RunnablePassthrough()}
        | prompt
        | model
        | output_parser
)


def execute_mixtral(request):
    print(request)
    response = chain.invoke(request)
    print(response)
    return response


# print(execute_star_coder_2("Create a fully functional DNN using Tensorflow and Keras to analyse the MNIST dataset."))
