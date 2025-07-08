import os
os.environ["CHROMA_ANONYMIZED_TELEMETRY"] = "False"
from llm import llm
from prompt import prompt
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from db import vector_store
from dotenv import load_dotenv

class ChatBot():

    load_dotenv()
    rag_chain = ({"context": vector_store.as_retriever(search_type="mmr"),  "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser())
    
bot = ChatBot()
print(bot.rag_chain.invoke("what is this document about?"))

