import os
from dotenv import load_dotenv
from langchain_community.vectorstores.chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'

persistent_dir = 'chroma_store'

vectorstore = Chroma(persist_directory=persistent_dir,
                     embedding_function=OpenAIEmbeddings())

retriever = vectorstore.as_retriever()

template = """Answer the question based only on the following context:
    {context}
    produce the answer in the following format:
    
    - point form
    - do not exceed 200 words
    - do not generate other information and just the answer to the query
    
    if you can't find the answer, just return "Answer not found in the context"
    Question: {question}
    
    """
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(model="gpt-4-1106-preview")

output_parser = StrOutputParser()

setup_and_retrieval = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
)

chain = (setup_and_retrieval
         | prompt
         | model
         | output_parser)


def reader(request):
    response = chain.invoke(request)
    return response


# req = "Whats the cost benefit analysis of auto code generation?"
# print(reader(req))
