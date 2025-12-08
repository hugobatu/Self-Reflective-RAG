from langgraph.graph import StateGraph, END
from state import AgentState
from modules.retrieval import retrieve_node
from modules.generation import generate_node
from modules.grading import grade_node
from modules.reflection import reflect_node
from graph import route_decision

# 1. Khởi tạo Workflow
workflow = StateGraph(AgentState)

# 2. Thêm các Nodes
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)
workflow.add_node("grade", grade_node)
workflow.add_node("reflect", reflect_node)

# 3. Định nghĩa Entry Point (Điểm bắt đầu)
workflow.set_entry_point("retrieve")

# 4. Định nghĩa các Cạnh (Edges)
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "grade")
workflow.add_edge("reflect", "retrieve") # **VÒNG LẶP REFLEXION**

# 5. Định nghĩa Cạnh Có Điều kiện (Conditional Edge)
workflow.add_conditional_edges(
    "grade",             # Node này chạy xong sẽ rẽ nhánh
    route_decision,      # Hàm quyết định (PASS -> END, FAIL -> reflect)
    {
        "reflect": "reflect",
        "end": END
    }
)

# 6. Biên dịch Graph
app = workflow.compile()