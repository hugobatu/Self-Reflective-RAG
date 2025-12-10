# server.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes

from app import app as graph_app 

load_dotenv()

app = FastAPI(
    title="Reflexion RAG Server",
    version="1.0",
    description="A simple testing API server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    graph_app,
    path="/reflexion",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)