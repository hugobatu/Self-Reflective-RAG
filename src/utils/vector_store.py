from langchain_chroma import Chroma
from langchain_core.documents import Document
from pathlib import Path
from typing import List
from embedding import LOCAL_EMEBDDING

# indexing data with embedding model
def index_data_with_local_embeddings(docs: List[Document]):
    embedding_function = LOCAL_EMEBDDING
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
    embedding_function = LOCAL_EMEBDDING
    persist_directory = Path("../../data/chroma_db_hotpotqa").resolve()

    db = Chroma(
        persist_directory=str(persist_directory),
        embedding_function=embedding_function
    )
    return db.as_retriever(search_kwargs={"k": 5})