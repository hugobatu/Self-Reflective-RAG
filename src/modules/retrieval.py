from utils.vector_store import get_retriever
from state import AgentState

def retrieve_node(state: AgentState) -> AgentState:
    # Quyết định dùng question gốc hay new_query sau khi reflect
    query = state["question"]
    
    retriever = get_retriever()
    retrieved_docs = retriever.invoke(query)
    
    # Chuyển đổi docs thành list string đơn giản để lưu vào state
    state["documents"] = [doc.page_content for doc in retrieved_docs]
    state["new_query"] = "" # clean the new query after usage
    
    return state