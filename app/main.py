"""
FastAPI application entrypoint for Naija Eats.

Registers all API routes and initialises application-level middleware.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Naija Eats",
    description=(
        "AI-powered behavioral simulation system that learns how individual users "
        "review restaurants — then predicts and writes reviews in their unique voice "
        "for places they have never visited."
    ),
    version="0.1.0",
)


# ---------------------------------------------------------------------------
# Health check
# ---------------------------------------------------------------------------


@app.get("/health", tags=["health"])
async def health_check() -> dict:
    """Return service liveness status."""
    return {"status": "ok"}


# ---------------------------------------------------------------------------
# TODO: Register feature routers once implemented
# ---------------------------------------------------------------------------
# from app.routers import reviews, users
# app.include_router(reviews.router)
# app.include_router(users.router)
