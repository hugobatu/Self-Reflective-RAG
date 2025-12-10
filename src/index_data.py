from utils.vector_store import index_data_with_local_embeddings
from utils.transforming import transform_hotpotqa_to_documents
from pathlib import Path

HOTPOTQA_RAW_PATH = "../data/hotpot_qa_raw" 

def main():
    if not Path(HOTPOTQA_RAW_PATH).exists():
        print(f"!!! LỖI: Không tìm thấy dữ liệu thô tại {HOTPOTQA_RAW_PATH}")
        print("Vui lòng chạy script tải dữ liệu (load_dataset) trước.")
        return
    
    print("Bắt đầu chuẩn hóa dữ liệu HotpotQA...")
    docs_to_index = transform_hotpotqa_to_documents(HOTPOTQA_RAW_PATH)
    print(f"Đã chuẩn hóa {len(docs_to_index)} Documents. Bắt đầu Indexing...")
    
    # Thực hiện indexing và tạo ChromaDB
    db = index_data_with_local_embeddings(docs_to_index)
    
if __name__ == "__main__":
    main()