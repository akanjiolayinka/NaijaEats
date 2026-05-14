"""
LLM review generation module for Naija Eats.

Orchestrates the reasoning chain using LangChain and Claude Sonnet.
Takes the user's behavioral fingerprint, their retrieved similar reviews,
and the new restaurant details — then produces a predicted star rating,
a voice-matched written review, a confidence score, and a reasoning trace.
"""

# TODO: from langchain_anthropic import ChatAnthropic
# TODO: from langchain.prompts import PromptTemplate
# TODO: from app.config import settings
# TODO: from app.profiler import BehavioralFingerprint
# TODO: from app.schemas import SimulateReviewResponse


class ReviewGenerator:
    """LLM reasoning agent that generates voice-matched reviews."""

    def __init__(self):
        # TODO: Initialise ChatAnthropic with settings.llm_model and settings.anthropic_api_key.
        # TODO: Load prompt template from models/prompts/review_generation.txt.
        pass

    def generate(
        self,
        fingerprint,  # BehavioralFingerprint
        retrieved_reviews: list[dict],
        restaurant: dict,
    ) -> dict:
        """
        Generate a simulated review for a restaurant based on user fingerprint.

        Args:
            fingerprint: The user's behavioral fingerprint.
            retrieved_reviews: Top-K semantically similar past reviews.
            restaurant: Dict of restaurant details (name, category, tags, etc.).

        Returns:
            Dict with keys: predicted_rating, review_text, confidence, reasoning.
        """
        # TODO: Construct the prompt by filling the template with fingerprint + context.
        # TODO: Call the LLM via LangChain.
        # TODO: Parse structured output (rating, review, confidence, reasoning).
        # TODO: Validate that predicted_rating is in range [1, 5].
        raise NotImplementedError
