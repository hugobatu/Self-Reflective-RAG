from state import AgentState
from chains.llm_clients import get_reasoning_llm

def reflect_node(state: AgentState) -> AgentState:
    llm = get_reasoning_llm()
    
    # Prompt để LLM suy ngẫm và tạo Query mới
    reflect_prompt = f"""Lần thử trước đã thất bại vì lỗi: {state['reflection']}.
    CÂU HỎI GỐC: {state['question']}.
    Hãy phân tích lỗi và tạo ra một CÂU HỎI TÌM KIẾM MỚI (chỉ 1 câu) tốt hơn để tìm kiếm lại thông tin còn thiếu.
    Query mới của bạn:"""
    
    new_query = llm.invoke(reflect_prompt).content
    state["new_query"] = new_query
    
    return state