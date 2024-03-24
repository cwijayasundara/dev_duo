import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores.chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

load_dotenv()

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'

loader = TextLoader('../docs/matt_transcript.txt')
docs = loader.load()

persistent_dir = '../chroma_store'
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=50)
splits = text_splitter.split_documents(docs)

# save the splits
vectorstore = Chroma.from_documents(documents=splits,
                                    persist_directory=persistent_dir,
                                    embedding=OpenAIEmbeddings())

vectorstore.persist()
