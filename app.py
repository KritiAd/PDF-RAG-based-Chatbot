# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from ragchain import ChatBot

bot = ChatBot()


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, RAG Chatbot is alive!"}

class QueryRequest(BaseModel):
    query: str
    file_path: Optional[str] = None

@app.get("/ask_question")
def query_doc(question : str):
    return bot.rag_chain.invoke(question)

