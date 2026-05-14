"""
Ablation study scripts for Naija Eats.

Measures the contribution of each system component by disabling it
and comparing performance against the full pipeline.

Components under ablation:
  1. Behavioral fingerprint (vs no profile — raw LLM)
  2. Retrieval layer (vs no retrieval — zero-shot)
  3. Cultural adaptation layer (vs no Nigerianizer)

Usage:
    python -m evaluation.ablation
"""

# TODO: from evaluation.metrics import compute_rmse, compute_bert_score


def run_ablation(dataset_path: str) -> dict:
    """
    Run all ablation conditions and return comparative results.

    Args:
        dataset_path: Path to evaluation dataset.

    Returns:
        Dict mapping condition name to metric results.
    """
    # TODO: Define ablation conditions:
    #   - "full_pipeline": all components enabled
    #   - "no_fingerprint": skip profiler, pass empty profile
    #   - "no_retrieval": skip retriever, pass empty retrieved_reviews
    #   - "no_cultural_layer": set enable_cultural_layer=False

    # TODO: For each condition, generate predictions and compute metrics.
    # TODO: Return results dict for reporting.
    raise NotImplementedError


if __name__ == "__main__":
    results = run_ablation("data/processed/eval_set.parquet")
    print(results)
