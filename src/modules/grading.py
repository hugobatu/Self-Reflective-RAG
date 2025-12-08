from state import AgentState
from chains.llm_clients import get_reasoning_llm

def grade_node(state: AgentState) -> AgentState:
    llm = get_reasoning_llm()
    
    # Prompt yêu cầu LLM đóng vai giám khảo (Critic)
    grading_prompt = f"""Bạn là một chuyên gia đánh giá RAG. 
    Dựa trên TÀI LIỆU và CÂU HỎI, hãy đánh giá CÂU TRẢ LỜI.
    - Tiêu chí: CÂU TRẢ LỜI có bị ẢO GIÁC (HALLUCINATION) so với TÀI LIỆU không?
    - Trả lời CHỈ MỘT TỪ: "PASS" (Nếu đáp án dựa trên tài liệu) hoặc "FAIL" (Nếu có sai sót/ảo giác).
    ---
    CÂU HỎI: {state['question']}
    TÀI LIỆU: {state['documents']}
    CÂU TRẢ LỜI: {state['generation']}
    ---
    Đánh giá (PASS/FAIL):"""
    
    grade = llm.invoke(grading_prompt).content.strip().upper()
    state["grade"] = grade
    
    # Nếu FAIL, cần LLM giải thích lỗi để Reflect
    if grade == "FAIL":
        # Sinh ra lời phê bình (Reflection)
        reflect_prompt = "Tại sao câu trả lời trên FAIL? Hãy nêu ra lỗi sai ngắn gọn."
        reflection = llm.invoke(reflect_prompt).content
        state["reflection"] = reflection
        
    return state