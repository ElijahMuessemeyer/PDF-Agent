from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.schema import BaseRetriever

def build_qa_chain(retriever: BaseRetriever) -> RetrievalQA:
    llm = ChatOpenAI(temperature=0)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
