import os
from dotenv import load_dotenv
# Import các thành phần cần thiết
from main import app 
from state import AgentState 
# Import hàm để load ChromaDB (nếu cần kiểm tra)

# 1. Load biến môi trường (API Keys)
load_dotenv() 

# 2. Định nghĩa câu hỏi thử nghiệm (Nên dùng câu hỏi multi-hop từ HotpotQA)
test_question = "Which magazine was started first Arthur's Magazine or First for Women?"

# 3. Khởi tạo Trạng thái Ban đầu
# LangGraph luôn cần một trạng thái khởi tạo (initial state)
initial_state = AgentState(
    question=test_question,
    documents=[],
    generation="",
    revision_number=0,
    reflection="",
    new_query="",
    grade="FAIL" # Set mặc định là FAIL để quá trình chạy bắt đầu
)

print(f"--- BẮT ĐẦU CHẠY SELF-CORRECTION RAG ---")
print(f"CÂU HỎI: {test_question}\n")

# 4. Thực thi LangGraph
# Sử dụng stream để xem từng bước chạy (step) một
for step in app.stream(initial_state):
    # step là một dict, key là tên node đang chạy, value là state sau khi node đó hoàn thành
    
    node_name = list(step.keys())[0]
    output_state = step[node_name]
    
    print(f"[{node_name.upper()}] chạy xong.")
    
    # In ra các thay đổi quan trọng
    if 'documents' in output_state:
        print(f"  -> DOCUMENTS: Đã tìm thấy {len(output_state['documents'])} đoạn văn.")
    if 'generation' in output_state and output_state['generation']:
        print(f"  -> DRAFT ANSWER: {output_state['generation'][:100]}...")
    if 'grade' in output_state and output_state['grade']:
        print(f"  -> GRADE: {output_state['grade']}")
    if 'reflection' in output_state and output_state['reflection']:
        print(f"  -> REFLECTION: {output_state['reflection']}")
    if 'new_query' in output_state and output_state['new_query']:
        print(f"  -> NEW QUERY: {output_state['new_query']}")
    
    print("-" * 20)
    
# 5. Lấy kết quả cuối cùng (Final Result)
final_result = app.invoke(initial_state)
print("\n=== KẾT QUẢ CUỐI CÙNG SAU KHI SỬA LỖI ===")
print(final_result['generation'])