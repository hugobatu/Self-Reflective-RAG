from langchain_huggingface import HuggingFaceEmbeddings

def get_local_embedding_model():
    model_name = "BAAI/bge-m3"
    model_kwargs = {'device': 'cuda'}
    encode_kwargs = {'normalize_embeddings': True}
    
    embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    return embeddings

LOCAL_EMEBDDING = get_local_embedding_model()