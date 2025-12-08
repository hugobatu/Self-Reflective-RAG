from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from pathlib import Path
from typing import List

def get_local_embedding_model():
    model_name = "BAAI/bge-m3"
    model_kwargs = {'device': 'cuda'}
    encode_kwargs = {'normalize_embeddings': True}
    
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return embeddings

def index_data_with_local_embeddings(docs: List[Document]):
    embedding_function = get_local_embedding_model()
    persist_directory = Path("../data/chroma_db_hotpotqa").resolve()

    print("Bắt đầu indexing dữ liệu bằng embedding local...")
    db = Chroma.from_documents(
        documents=docs,
        embedding=embedding_function,
        persist_directory=str(persist_directory)
    )
    db.persist()
    print(f"Indexing hoàn tất. Dữ liệu đã lưu tại {persist_directory}")
    return db

def get_retriever():
    embedding_function = get_local_embedding_model()
    persist_directory = Path("../../data/chroma_db_hotpotqa").resolve()

    db = Chroma(
        persist_directory=str(persist_directory),
        embedding_function=embedding_function
    )
    return db.as_retriever(search_kwargs={"k": 5})