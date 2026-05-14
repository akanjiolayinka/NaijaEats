"""
Embedding utilities for Naija Eats.

Wraps sentence-transformers to provide a consistent embedding interface
used by both the indexing pipeline and the retrieval layer.
"""

# TODO: from sentence_transformers import SentenceTransformer
# TODO: import numpy as np
# TODO: from app.config import settings


class EmbeddingModel:
    """Thin wrapper around a sentence-transformer model."""

    def __init__(self, model_name: str | None = None):
        # TODO: Load SentenceTransformer(model_name or settings.embedding_model).
        pass

    def embed(self, texts: list[str]) -> list:  # -> list[np.ndarray]
        """
        Compute embeddings for a list of texts.

        Args:
            texts: Strings to embed.

        Returns:
            List of numpy arrays, one per input text.
        """
        # TODO: Call self.model.encode(texts, show_progress_bar=False).
        raise NotImplementedError

    def embed_single(self, text: str) -> object:  # -> np.ndarray
        """
        Convenience wrapper to embed a single string.

        Args:
            text: String to embed.

        Returns:
            1-D numpy array.
        """
        # TODO: Return self.embed([text])[0].
        raise NotImplementedError
