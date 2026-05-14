"""
Human evaluation framework for Naija Eats.

Supports collecting human judgements on whether generated reviews are:
  - Stylistically indistinguishable from the real user's reviews
  - Culturally authentic (Nigerian voice, appropriate Pidgin level)
  - Factually plausible given the restaurant description

Target: > 80% of reviews rated as "authentic" by human evaluators.
"""

# TODO: import pandas as pd


def prepare_evaluation_batch(
    generated_reviews: list[dict],
    real_reviews: list[dict],
    batch_size: int = 50,
) -> list[dict]:
    """
    Prepare a mixed batch of generated and real reviews for blind evaluation.

    Interleaves generated and real reviews so evaluators cannot identify which
    is which based on ordering.

    Args:
        generated_reviews: Model-generated reviews with user_id and review_text.
        real_reviews: Actual user reviews used as ground truth.
        batch_size: Number of items per evaluation batch.

    Returns:
        List of dicts ready for human annotation.
    """
    # TODO: Interleave generated and real reviews randomly.
    # TODO: Assign an anonymous ID to each item.
    # TODO: Remove metadata that would reveal which is real vs generated.
    raise NotImplementedError


def compute_authenticity_score(annotations: list[dict]) -> float:
    """
    Compute the fraction of generated reviews judged as authentic.

    Args:
        annotations: List of human annotation dicts with 'is_authentic' bool field.

    Returns:
        Authenticity rate between 0.0 and 1.0.
    """
    # TODO: Filter to generated reviews only and compute mean is_authentic.
    raise NotImplementedError
