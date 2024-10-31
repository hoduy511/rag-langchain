from typing import Dict, List

from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentFormatter:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200, separators=["\n\n", "\n", ".", " ", ""]
        )

    def format_document(self, content: str, metadata: Dict) -> List[Document]:
        content = content.encode("utf-8", errors="ignore").decode("utf-8")
        content = " ".join(content.split())
        content = content.replace("\r\n", "\n")
        content = "".join(char for char in content if char.isprintable())

        metadata["format_version"] = "1.0"
        metadata["chunk_size"] = self.text_splitter._chunk_size
        metadata["chunk_overlap"] = self.text_splitter._chunk_overlap

        chunks = self.text_splitter.split_text(content)

        documents = []
        for i, chunk in enumerate(chunks):
            chunk_metadata = metadata.copy()
            chunk_metadata["chunk_id"] = i
            documents.append(Document(page_content=chunk, metadata=chunk_metadata))

        return documents
