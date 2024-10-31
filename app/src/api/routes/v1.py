from fastapi import APIRouter, File, UploadFile, HTTPException
from src.services.pdf_service import PDFService
from src.models.schemas import QueryRequest, QueryResponse, DocumentProcessingResponse
from src.chains.rag_chain import RAGChain
from src.services.vector_store import VectorStoreService

router = APIRouter()
rag_chain = RAGChain()


@router.post("/upload", response_model=DocumentProcessingResponse)
async def upload_pdf(file: UploadFile = File(...)):
    pdf_service = PDFService()
    file_path = await pdf_service.save_pdf(file)
    if file.filename is None:
        raise HTTPException(status_code=400, detail="Filename is required")
    result = await pdf_service.process_pdf(file_path, file.filename)
    return DocumentProcessingResponse(**result)


@router.post("/query", response_model=QueryResponse)
async def query_documents(request: QueryRequest):
    try:
        chain = rag_chain.get_chain()
        answer = await chain.ainvoke(request.question)
        return QueryResponse(answer=answer, sources=[])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


@router.post("/search")
async def similarity_search(query: str, k: int = 4):
    vector_store = VectorStoreService()
    results = vector_store.similarity_search(query, k=k)
    return {"query": query, "results": results}
