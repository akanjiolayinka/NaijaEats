"""
Pydantic request/response models for the Naija Eats API.

Defines the contract between API consumers and the service.
"""

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Request models
# ---------------------------------------------------------------------------


class Restaurant(BaseModel):
    """Details of the restaurant to generate a simulated review for."""

    name: str
    category: str
    price_range: str
    location: str
    menu_highlights: list[str] = Field(default_factory=list)
    common_tags: list[str] = Field(default_factory=list)

    # TODO: Add optional fields such as average_rating, opening_hours, photos_url.


class SimulateReviewRequest(BaseModel):
    """Payload for POST /simulate-review."""

    user_id: str
    restaurant: Restaurant

    # TODO: Add optional override fields (e.g. force_cultural_layer, top_k).


# ---------------------------------------------------------------------------
# Response models
# ---------------------------------------------------------------------------


class SimulateReviewResponse(BaseModel):
    """Response from POST /simulate-review."""

    user_id: str
    predicted_rating: int = Field(..., ge=1, le=5)
    review_text: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    reasoning: str

    # TODO: Add retrieved_reviews field exposing the top-K similar past reviews used.


class UserProfileResponse(BaseModel):
    """Response from GET /users/{user_id}/profile."""

    user_id: str
    profile: dict  # TODO: Replace with a typed BehavioralFingerprint model.


class HealthResponse(BaseModel):
    """Response from GET /health."""

    status: str
