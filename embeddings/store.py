from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

vectorstore = None

def create_vectorstore(chunks: list[str], embedding_model: OpenAIEmbeddings) -> FAISS:
    return FAISS.from_texts(texts=chunks, embedding=embedding_model)
