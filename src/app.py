from langgraph.graph import StateGraph, END
from state import AgentState
from modules.retrieval import retrieve_node
from modules.generation import generate_node
from modules.grading import grade_node
from modules.reflection import reflect_node
from modules.graph import route_decision

# creating workflow with agent state
workflow = StateGraph(AgentState)

# craeting nodes in workflow
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)
workflow.add_node("grade", grade_node)
workflow.add_node("reflect", reflect_node)

# defining the entry point: retrieve
workflow.set_entry_point("retrieve")

# defining edges
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "grade")
workflow.add_edge("reflect", "retrieve") # **VÒNG LẶP REFLEXION**

# 5. conditional edges
workflow.add_conditional_edges(
    "grade", # node này chạy xong sẽ rẽ nhánh
    route_decision, # decision function to check when to pass if not passed, then marked fail and reflect
    {
        "reflect": "reflect",
        "end": END
    }
)

# compile graph
app = workflow.compile()