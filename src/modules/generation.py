from chains.llm_clients import get_reasoning_llm
from modules.retrieval import AgentState

def generate_node(state: AgentState) -> AgentState:
    llm = get_reasoning_llm()
    
    prompt = f"""Bạn là trợ lý RAG. Hãy sử dụng những tài liệu sau đây để trả lời câu hỏi:
    ---
    Tài liệu: {state['documents']}
    ---
    Câu hỏi: {state['question']}
    ---
    Câu trả lời của bạn:"""
    
    response = llm.invoke(prompt)
    state["generation"] = response.content
    state["revision_number"] += 1 # Tăng số lần thử
    return state