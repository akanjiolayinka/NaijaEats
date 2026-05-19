"""
Vector similarity retrieval module for Naija Eats.

Uses sentence-transformers to embed user reviews and ChromaDB as the vector
store. At inference time, retrieves the top-K past reviews most semantically
similar to the new restaurant description, grounding the LLM in real user
behavior rather than abstract generalisation.
"""

from sentence_transformers import SentenceTransformer
import chromadb
from app.config import settings
import os


class ReviewRetriever:
    """Manages the ChromaDB collection and similarity search for user reviews."""

    def __init__(self):
        # We wrap this in a try-except because sentence-transformers might 
        # try to download the model, which could fail without internet or take too long.
        try:
            self.model = SentenceTransformer(settings.embedding_model)
        except Exception:
            self.model = None
            
        try:
            self.client = chromadb.PersistentClient(path=settings.chroma_persist_dir)
            self.collection = self.client.get_or_create_collection(name="user_reviews")
        except Exception:
            self.client = None
            self.collection = None

    def index_reviews(self, user_id: str, reviews: list[dict]) -> None:
        """
        Embed and store a user's reviews in the vector store.
        """
        if not self.collection or not self.model:
            return

        texts = [r["text"] for r in reviews]
        ids = [str(r.get("review_id", i)) for i, r in enumerate(reviews)]
        metadatas = [{"user_id": user_id, "stars": r["stars"]} for r in reviews]
        
        embeddings = self.model.encode(texts).tolist()
        
        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=texts
        )

    def retrieve_similar(
        self,
        user_id: str,
        query: str,
        top_k: int | None = None,
    ) -> list[dict]:
        """
        Find the top-K reviews most similar to the query string.
        """
        if not self.collection or not self.model:
            # Fallback to empty list if ChromaDB is not ready
            return []

        k = top_k or settings.top_k_retrieval
        
        query_embedding = self.model.encode([query]).tolist()[0]
        
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
            where={"user_id": user_id}
        )
        
        formatted_results = []
        if results["documents"]:
            for i in range(len(results["documents"][0])):
                formatted_results.append({
                    "text": results["documents"][0][i],
                    "metadata": results["metadata"][0][i],
                    "distance": results["distances"][0][i] if "distances" in results else None
                })
        
        return formatted_results
