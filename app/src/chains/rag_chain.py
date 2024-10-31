from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.services.llm_service import LLMService
from src.services.vector_store import VectorStoreService


class RAGChain:
    def __init__(self):
        # Initialize services
        self.vector_store = VectorStoreService()
        self.llm_service = LLMService()

        # Get components
        self.retriever = self.vector_store.get_retriever(
            search_type="similarity", k=10, score_threshold=0.7
        )
        self.llm = self.llm_service.get_llm()

        # Create prompt template
        self.prompt = hub.pull("rlm/rag-prompt")

    def get_chain(self):
        # Build the chain
        chain = (
            {"context": self.retriever, "question": RunnablePassthrough()}
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
        return chain
