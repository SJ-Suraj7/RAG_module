import os
import chainlit as cl
from langchain import HuggingFaceHub, PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from dataloader import *

'''
ADD huggingface_hub token for Open Source LLMs
#os.environ['API_KEY'] = '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'

'''

'''
#USING OPEN SOURCE LLM MODELS
model_id = 'tiiuae/falcon-7b-instruct'
llm = HuggingFaceHub(huggingface_hub_api_token='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',
                     repo_id=model_id,
                     model_kwargs={"temperature":0.8, "max_new_tokens":100}
                     )


chain = LLMChain(llm=llm,
                 #prompt = prompt,
                 verbose=True)

'''

os.environ["OPENAI_API_KEY"] = "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"
model_name = "gpt-3.5-turbo"
llm = ChatOpenAI(model_name=model_name)


chain = load_qa_chain(llm, chain_type="stuff", verbose=True)

query = "What are the required documents for issuing a pan card"
matching_docs = db.similarity_search(query)
answer = chain.run(
    input_documents=matching_docs,
    question=query)
print(answer)


