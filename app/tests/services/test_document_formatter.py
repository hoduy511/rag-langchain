import pytest
from src.services.document_formatter import DocumentFormatter


class TestDocumentFormatter:
    @pytest.fixture
    def formatter(self):
        return DocumentFormatter()

    def test_format_document(self, formatter):
        content = "Sample content from PDF\nMultiple lines\nFor testing"
        metadata = {"source": "sample.pdf", "page": 1}

        docs = formatter.format_document(content, metadata)
        assert len(docs) > 0
        assert docs[0].metadata["format_version"] == "1.0"
        assert "chunk_id" in docs[0].metadata
