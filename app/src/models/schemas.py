from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str
    sources: Optional[List[str]] = None


class DocumentProcessingResponse(BaseModel):
    status: str
    chunks: int
    filename: str
    processing_details: Optional[Dict[str, Any]] = None
    document_stats: Optional[Dict[str, int]] = None
