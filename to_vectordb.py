from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from config import embedding_model_name
from dataloader import docs

'''create embedding vectors'''
embeddings = SentenceTransformerEmbeddings(model_name=embedding_model_name)

'''Store embedding vectors to vector DB. Vector DB used is Chroma'''
db = Chroma.from_documents(docs, embeddings)
