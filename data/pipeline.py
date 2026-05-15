"""
Data loading and preprocessing pipeline for Naija Eats.

Handles downloading, filtering, and transforming the Yelp Open Dataset
into the format expected by the profiler and retrieval modules.

Usage:
    python -m data.pipeline --download --process
"""

import argparse
import pandas as pd
import os


def seed_mock_data():
    """Create mock processed data for testing."""
    os.makedirs("data/processed", exist_ok=True)
    
    # Mock reviews for Bayo
    reviews = [
        {
            "review_id": "r1",
            "user_id": "bayo_001",
            "business_id": "b1",
            "stars": 5,
            "text": "This amala is the best I've had in Lagos. E dey slap! Highly recommend.",
            "date": "2024-01-01"
        },
        {
            "review_id": "r2",
            "user_id": "bayo_001",
            "business_id": "b2",
            "stars": 2,
            "text": "The food was okay but the service was so slow. I waited for 40 minutes. Abeg, they need to fix up.",
            "date": "2024-01-05"
        },
        {
            "review_id": "r3",
            "user_id": "bayo_001",
            "business_id": "b3",
            "stars": 4,
            "text": "Good vibes and good food. The jollof was on point.",
            "date": "2024-01-10"
        }
    ]
    
    df = pd.DataFrame(reviews)
    df.to_parquet("data/processed/reviews.parquet")
    print("Mock data seeded to data/processed/reviews.parquet")


def main() -> None:
    parser = argparse.ArgumentParser(description="Naija Eats data pipeline")
    parser.add_argument("--download", action="store_true", help="Download raw dataset")
    parser.add_argument("--process", action="store_true", help="Process raw data")
    parser.add_argument("--seed", action="store_true", help="Seed mock data")
    args = parser.parse_args()

    if args.seed:
        seed_mock_data()
    elif args.download:
        print("Download not yet implemented.")
    elif args.process:
        print("Process not yet implemented.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
