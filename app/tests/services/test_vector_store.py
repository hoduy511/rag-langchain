import pytest
from langchain_core.documents import Document
from src.services.vector_store import VectorStoreService


class TestVectorStore:
    @pytest.fixture
    def vector_store(self):
        return VectorStoreService()

    def test_add_documents(self, vector_store):
        docs = [
            Document(
                page_content="Content from sample PDF",
                metadata={"source": "sample.pdf", "page": 1, "format_version": "1.0"},
            )
        ]
        result = vector_store.add_documents(docs)
        assert result is not None

    def test_similarity_search(self, vector_store):
        results = vector_store.similarity_search("sample content", k=2)
        assert isinstance(results, list)

    def test_get_retriever(self, vector_store):
        retriever = vector_store.get_retriever(k=3)
        assert retriever is not None
        assert retriever.search_kwargs["k"] == 3
