import pytest
from src.services.pdf_service import PDFService


class TestPDFService:
    @pytest.fixture
    def pdf_service(self):
        return PDFService()

    @pytest.fixture
    def sample_pdf_path(self):
        return "app/tests/data/sample.pdf"

    @pytest.mark.asyncio
    async def test_process_pdf_success(self, pdf_service, sample_pdf_path):
        result = await pdf_service.process_pdf(sample_pdf_path, "sample.pdf")

        assert result["status"] == "success"
        assert result["chunks"] > 0
        assert result["filename"] == "sample.pdf"

    @pytest.mark.asyncio
    async def test_process_pdf_invalid_path(self, pdf_service):
        with pytest.raises(Exception):
            await pdf_service.process_pdf("/invalid/path.pdf", "invalid.pdf")
