from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from langchain_community.embeddings import OpenAIEmbeddings

def get_embedding_model() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(openai_api_key=api_key)

def embed_chunks(chunks: list[str]) -> list[list[float]]:
    return embeddings.embed_chunks(chunks)
