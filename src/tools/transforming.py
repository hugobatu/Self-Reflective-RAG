from datasets import load_from_disk
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma

def transform_hotpotqa_to_documents(dataset_path: str):
    """Tải dữ liệu HotpotQA và chuyển đổi thành List[Document] của LangChain."""
    
    # dataset = load_from_disk(dataset_path)['train']
    
    raw_dataset = load_from_disk(dataset_path)['train'].select(range(200))
    print("Question:", raw_dataset[:100]['question'])
    print("Raw:", raw_dataset[:100]['answer'])

    documents = []
    for num, example in enumerate(raw_dataset):
        question = example['question']
        
        # nối các đoạn văn: tên tài liệu + các câu
        context_parts = []
        for title, sentences in zip(example['context']['title'], example['context']['sentences']):
            # link tiêu đề và nội dung để làm một chunk
            context_text = f"Tài liệu: {title}\nNội dung: {' '.join(sentences)}"
            context_parts.append(context_text)
            
        # tạo một Document cho mỗi câu hỏi và context đi kèm
        doc_content = "\n\n".join(context_parts)
        # if num < 5:
        #     print(f"Docs {num}", doc_content)

        # lưu cả câu hỏi và câu trả lời vào metadata để dùng cho bước đánh giá sau này
        doc = Document(
            page_content=doc_content,
            metadata={
                "question": question,
                "answer": example['answer'],
                "doc_id": example['id']
            }
        )
        documents.append(doc)
    
    return documents

# docs_to_index = transform_hotpotqa_to_documents("../../data/hotpot_qa_raw")
# print(f"Đã tạo {len(docs_to_index)} Document.")