from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient, models
from src.core.config import settings


class VectorStoreService:
    def __init__(self):
        self.client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
        self.embedding = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={"token": settings.HUGGINGFACE_TOKEN},
        )
        self._create_collection()
        self.vectorstore = QdrantVectorStore(
            client=self.client,
            collection_name=settings.COLLECTION_NAME,
            embedding=self.embedding,
        )

    def _create_collection(self):
        collections = self.client.get_collections().collections
        collection_names = [c.name for c in collections]
        if settings.COLLECTION_NAME not in collection_names:
            self.client.create_collection(
                collection_name=settings.COLLECTION_NAME,
                vectors_config=models.VectorParams(
                    size=384,
                    distance=models.Distance.COSINE,
                ),
            )

    def similarity_search(self, query: str, k: int = 4, score_threshold: float = 0.7):
        query_vector = self.embedding.embed_query(query)
        results = self.client.search(
            collection_name=settings.COLLECTION_NAME,
            query_vector=query_vector,
            limit=k,
            score_threshold=score_threshold,
        )
        return results

    def get_retriever(self, **kwargs):
        search_kwargs = {
            "k": kwargs.get("k", 4),
            "score_threshold": kwargs.get("score_threshold", 0.7),
        }
        return self.vectorstore.as_retriever(search_kwargs=search_kwargs)

    def add_documents(self, documents):
        if not all(doc.metadata.get("format_version") for doc in documents):
            raise ValueError("Documents must be formatted before storage")
        return self.vectorstore.add_documents(documents)
