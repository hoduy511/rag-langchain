import pytest
from src.chains.rag_chain import RAGChain


class TestRAGChain:
    @pytest.fixture
    def rag_chain(self):
        return RAGChain()

    def test_chain_initialization(self, rag_chain):
        assert rag_chain.retriever is not None
        assert rag_chain.llm is not None
        assert rag_chain.prompt is not None

    @pytest.mark.asyncio
    async def test_chain_execution(self, rag_chain):
        chain = rag_chain.get_chain()
        result = await chain.ainvoke("What is the main topic in sample.pdf?")
        assert isinstance(result, str)
        assert len(result) > 0
