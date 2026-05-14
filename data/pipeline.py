"""
Data loading and preprocessing pipeline for Naija Eats.

Handles downloading, filtering, and transforming the Yelp Open Dataset
into the format expected by the profiler and retrieval modules.

Usage:
    python -m data.pipeline --download --process
"""

import argparse

# TODO: import pandas as pd
# TODO: from datasets import load_dataset  # HuggingFace datasets


def download_dataset(output_dir: str = "data/raw") -> None:
    """
    Download the Yelp Open Dataset.

    Args:
        output_dir: Directory to save raw files.
    """
    # TODO: Pull dataset via HuggingFace datasets or direct Yelp download.
    # TODO: Save raw JSON files to output_dir.
    raise NotImplementedError


def load_reviews(raw_path: str) -> object:  # -> pd.DataFrame
    """
    Load raw Yelp reviews JSON into a DataFrame.

    Args:
        raw_path: Path to yelp_academic_dataset_review.json.

    Returns:
        DataFrame with columns: review_id, user_id, business_id, stars, text, date.
    """
    # TODO: Read JSONL file with pd.read_json(..., lines=True).
    # TODO: Select and rename relevant columns.
    raise NotImplementedError


def load_businesses(raw_path: str) -> object:  # -> pd.DataFrame
    """
    Load raw Yelp business JSON into a DataFrame.

    Args:
        raw_path: Path to yelp_academic_dataset_business.json.

    Returns:
        DataFrame with columns: business_id, name, city, state, categories, stars.
    """
    # TODO: Read JSONL file and select relevant columns.
    raise NotImplementedError


def filter_active_users(reviews_df, min_reviews: int = 10) -> object:  # -> pd.DataFrame
    """
    Keep only users who have at least min_reviews reviews.

    Args:
        reviews_df: Full reviews DataFrame.
        min_reviews: Minimum review count threshold.

    Returns:
        Filtered DataFrame.
    """
    # TODO: Group by user_id, count reviews, filter by min_reviews.
    raise NotImplementedError


def save_processed(df, output_path: str) -> None:
    """
    Persist a processed DataFrame to the data/processed directory.

    Args:
        df: DataFrame to save.
        output_path: Destination path (parquet preferred).
    """
    # TODO: Save as parquet with df.to_parquet(output_path).
    raise NotImplementedError


def main() -> None:
    parser = argparse.ArgumentParser(description="Naija Eats data pipeline")
    parser.add_argument("--download", action="store_true", help="Download raw dataset")
    parser.add_argument("--process", action="store_true", help="Process raw data")
    args = parser.parse_args()

    if args.download:
        download_dataset()

    if args.process:
        # TODO: Orchestrate load -> filter -> save flow.
        raise NotImplementedError


if __name__ == "__main__":
    main()
