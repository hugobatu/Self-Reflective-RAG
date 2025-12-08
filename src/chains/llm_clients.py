from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage


def get_reasoning_llm(temperature=0.0):
    
    message = "Bạn là một Trợ lý RAG thông minh, luôn luôn kiểm tra tính đúng đắn của thông tin. Hãy trả lời một cách chi tiết và chính xác."
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=temperature,
        convert_system_message_to_human=True
    )
    llm.invoke(message)
    return llm