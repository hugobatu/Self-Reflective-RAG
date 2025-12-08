from state import AgentState

def route_decision(state: AgentState) -> str:
    """Kiểm tra điểm và số lần thử để quyết định luồng tiếp theo."""
    
    if state["grade"] == "PASS":
        print("--- ĐÁP ÁN ĐẠT CHẤT LƯỢNG. KẾT THÚC. ---")
        return "end" # END là hằng số kết thúc của LangGraph
    
    # Giới hạn số lần thử lại để tránh lặp vô hạn và tốn phí
    if state["revision_number"] >= 3:
        print("--- ĐÃ THỬ LẠI 3 LẦN. KẾT THÚC VỚI KẾT QUẢ HIỆN TẠI. ---")
        return "end"
    
    print(f"--- ĐÁP ÁN FAIL. CẦN REFLECT VÀ THỬ LẠI. Lần thử: {state['revision_number']} ---")
    return "reflect" # Chuyển sang bước suy ngẫm