from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes
from src.api.routes import v1
from src.chains.rag_chain import RAGChain
from src.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1.router, prefix=settings.API_V1_STR)

rag_chain = RAGChain()
add_routes(app, rag_chain.get_chain(), path="/rag")


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
