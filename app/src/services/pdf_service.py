import os
import tempfile

from fastapi import UploadFile
from langchain_community.document_loaders import PyPDFLoader
from src.services.document_formatter import DocumentFormatter
from src.services.vector_store import VectorStoreService


class PDFService:
    def __init__(self):
        self.vector_store = VectorStoreService()
        self.formatter = DocumentFormatter()

    async def save_pdf(self, file: UploadFile) -> str:
        """Save uploaded PDF file to temporary location"""
        try:
            # Create temporary file
            _, temp_path = tempfile.mkstemp(suffix=".pdf")

            # Write uploaded file content
            with open(temp_path, "wb") as temp_file:
                content = await file.read()
                temp_file.write(content)

            return temp_path

        except Exception as e:
            print(f"Error saving PDF: {e}")
            raise

    async def process_pdf(self, file_path: str, filename: str):
        try:
            loader = PyPDFLoader(file_path)
            raw_docs = loader.load()

            formatted_docs = []
            for doc in raw_docs:
                # Enhanced metadata
                metadata = {
                    "filename": filename,
                    "source": file_path,
                    "page": doc.metadata.get("page", 0),
                    "chunk_id": len(formatted_docs),
                }

                # Improved chunking with overlap
                formatted_chunks = self.formatter.format_document(
                    doc.page_content, metadata
                )
                formatted_docs.extend(formatted_chunks)

            self.vector_store.add_documents(formatted_docs)

            # Clean up temporary file
            os.remove(file_path)

            return {
                "status": "success",
                "chunks": len(formatted_docs),
                "filename": filename,
            }
        except Exception as e:
            print(f"Error processing PDF: {e}")
            raise
