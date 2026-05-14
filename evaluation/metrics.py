"""
Automated evaluation metrics for Naija Eats.

Measures three core dimensions of system quality:

  1. Rating Accuracy  — RMSE between predicted and ground-truth star ratings.
  2. Text Quality     — BERTScore F1 between generated and reference reviews.
  3. Style Fidelity   — ROUGE scores measuring n-gram overlap with user's real reviews.

Usage:
    python -m evaluation.metrics --run-all
"""

import argparse

# TODO: import numpy as np
# TODO: from sklearn.metrics import mean_squared_error
# TODO: from bert_score import score as bert_score
# TODO: from rouge_score import rouge_scorer


def compute_rmse(predicted_ratings: list[int], true_ratings: list[int]) -> float:
    """
    Compute RMSE between predicted and ground-truth ratings.

    Target: RMSE < 0.7.

    Args:
        predicted_ratings: List of model-predicted star ratings.
        true_ratings: List of actual star ratings from the dataset.

    Returns:
        RMSE value.
    """
    # TODO: return float(np.sqrt(mean_squared_error(true_ratings, predicted_ratings)))
    raise NotImplementedError


def compute_bert_score(
    generated_texts: list[str],
    reference_texts: list[str],
    lang: str = "en",
) -> dict:
    """
    Compute BERTScore F1 between generated and reference reviews.

    Target: BERTScore F1 > 0.85.

    Args:
        generated_texts: List of model-generated review strings.
        reference_texts: List of reference (ground-truth) review strings.
        lang: Language code for BERTScore model selection.

    Returns:
        Dict with keys: precision, recall, f1 (each as mean float).
    """
    # TODO: Call bert_score(generated_texts, reference_texts, lang=lang).
    # TODO: Return mean precision, recall, f1.
    raise NotImplementedError


def compute_rouge(
    generated_texts: list[str],
    reference_texts: list[str],
) -> dict:
    """
    Compute ROUGE-1, ROUGE-2, and ROUGE-L scores.

    Args:
        generated_texts: Model-generated review strings.
        reference_texts: Reference review strings.

    Returns:
        Dict with keys: rouge1, rouge2, rougeL (each as mean F1 float).
    """
    # TODO: Initialise rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL']).
    # TODO: Average scores across all pairs.
    raise NotImplementedError


def run_all(dataset_path: str) -> dict:
    """
    Run the full evaluation suite on a labeled dataset.

    Args:
        dataset_path: Path to evaluation dataset (parquet or JSON).

    Returns:
        Dict containing all metric results.
    """
    # TODO: Load dataset.
    # TODO: Generate predictions using the full pipeline.
    # TODO: Compute and print RMSE, BERTScore, ROUGE.
    raise NotImplementedError


def main() -> None:
    parser = argparse.ArgumentParser(description="Naija Eats evaluation metrics")
    parser.add_argument("--run-all", action="store_true", help="Run full evaluation suite")
    parser.add_argument("--dataset", default="data/processed/eval_set.parquet")
    args = parser.parse_args()

    if args.run_all:
        results = run_all(args.dataset)
        print(results)


if __name__ == "__main__":
    main()
