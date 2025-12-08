from typing import TypedDict, List

class AgentState(TypedDict):
    """Đại diện cho trạng thái chung của agent qua từng bước."""
    question: str                   # Câu hỏi gốc từ người dùng
    documents: List[str]            # List các đoạn văn (context) tìm được
    generation: str                 # Câu trả lời (draft hoặc final)
    revision_number: int            # Số lần đã thử lại (Bắt đầu từ 0)
    reflection: str                 # Phản hồi từ Evaluator (Lý do cần sửa)
    new_query: str                  # Query mới được sinh ra sau khi Reflect
    grade: str                      # Kết quả đánh giá: "PASS" hoặc "FAIL"