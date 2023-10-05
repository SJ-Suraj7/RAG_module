from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import *


'''Load documents from data directory'''
def load_docs(directory):
    loader = DirectoryLoader(directory)
    documents = loader.load()
    return documents


'''
function for DATA SPLITTER:
splitting docs based on paragraph, line breaks
'''

def split_docs(documents,chunk_size=1000,chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs


directory = DIRECTORY
documents = load_docs(directory)
docs = split_docs(documents)
print(f'The data directory contains {len(docs)} documents')
