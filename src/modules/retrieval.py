from tools.vector_store import get_retriever # Retriever Local
from state import AgentState

def retrieve_node(state: AgentState) -> AgentState:
    # Quyết định dùng question gốc hay new_query sau khi reflect
    query = state.get("new_query") or state["question"]
    
    retriever = get_retriever()
    retrieved_docs = retriever.invoke(query)
    
    # Chuyển đổi docs thành list string đơn giản để lưu vào state
    state["documents"] = [doc.page_content for doc in retrieved_docs]
    state["new_query"] = "" # Dọn dẹp new_query sau khi dùng
    
    return state