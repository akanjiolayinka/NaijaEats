"""
Vector similarity retrieval module for Naija Eats.

Uses sentence-transformers to embed user reviews and ChromaDB as the vector
store. At inference time, retrieves the top-K past reviews most semantically
similar to the new restaurant description, grounding the LLM in real user
behavior rather than abstract generalisation.
"""

# TODO: from sentence_transformers import SentenceTransformer
# TODO: import chromadb
# TODO: from app.config import settings


class ReviewRetriever:
    """Manages the ChromaDB collection and similarity search for user reviews."""

    def __init__(self):
        # TODO: Initialise SentenceTransformer with settings.embedding_model.
        # TODO: Initialise ChromaDB client with settings.chroma_persist_dir.
        # TODO: Get or create a collection per user (or one shared collection).
        pass

    def index_reviews(self, user_id: str, reviews: list[dict]) -> None:
        """
        Embed and store a user's reviews in the vector store.

        Args:
            user_id: Unique identifier for the user.
            reviews: List of review dicts with at least 'text', 'stars', and 'review_id'.
        """
        # TODO: Generate embeddings for each review text.
        # TODO: Upsert into ChromaDB with metadata (stars, user_id, review_id).
        raise NotImplementedError

    def retrieve_similar(
        self,
        user_id: str,
        query: str,
        top_k: int | None = None,
    ) -> list[dict]:
        """
        Find the top-K reviews most similar to the query string.

        Args:
            user_id: Restrict search to this user's reviews.
            query: Free-text description of the new restaurant.
            top_k: Number of results to return; defaults to settings.top_k_retrieval.

        Returns:
            List of review dicts ordered by descending similarity score.
        """
        # TODO: Embed the query text.
        # TODO: Run ChromaDB similarity search filtered by user_id.
        # TODO: Return results enriched with distance/score field.
        raise NotImplementedError
