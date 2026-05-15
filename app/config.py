"""
Application configuration for Naija Eats.

Loads all settings from environment variables (via .env) using pydantic-settings.
All tuneable knobs for the system live here.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Top-level application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # --- API keys ---
    anthropic_api_key: str = ""
    openai_api_key: str = ""
    openrouter_api_key: str = ""

    # --- LLM ---
    llm_model: str = "claude-sonnet-4-20250514"

    # --- Embeddings ---
    embedding_model: str = "all-MiniLM-L6-v2"

    # --- Retrieval ---
    top_k_retrieval: int = 5

    # --- Profiling ---
    min_user_reviews: int = 10

    # --- Feature flags ---
    enable_cultural_layer: bool = True

    # --- Storage ---
    chroma_persist_dir: str = "./data/chroma"

    # --- Logging ---
    log_level: str = "INFO"


# Instantiate and export a single settings singleton used across all modules.
settings = Settings()
