"""
load_data.py

This file contains functions for loading the dataset.

The main responsibilities of this file are:

1. Define the project paths.
2. Find the raw dataset.
3. Define the processed dataset path.
4. Load the CSV file.
5. Return the dataset as a pandas DataFrame.

The code is intentionally written in a beginner-friendly way.
"""


# ============================================================
# IMPORTS
# ============================================================

from pathlib import Path

import pandas as pd


# ============================================================
# PROJECT PATH
# ============================================================

# Get the main project folder.
#
# __file__ points to this file.
# .parent points to the "src" folder.
# .parent.parent points to the main project folder.

PROJECT_PATH = Path(__file__).resolve().parent.parent


# ============================================================
# DATA PATHS
# ============================================================

# Path to the original/raw dataset.
RAW_DATA_PATH = (
    PROJECT_PATH
    / "data"
    / "raw"
    / "AI_SocialMedia_Student_Health_Dataset.csv"
)


# Path where the cleaned/processed dataset will be saved.

PROCESSED_DATA_PATH = (
    PROJECT_PATH
    / "data"
    / "processed"
    / "AI_SocialMedia_Student_Health_Dataset_clean.csv"
)


# ============================================================
# FUNCTION: LOAD DATA
# ============================================================

def load_data(file_path=RAW_DATA_PATH):
    """
    Load the dataset from a CSV file.

    Args:
        file_path:
            Path to the CSV dataset.

    Returns:
        pandas.DataFrame:
            The loaded dataset.

        None:
            If the dataset could not be loaded.
    """

    print("\n" + "=" * 70)
    print("LOADING DATASET")
    print("=" * 70)

    try:

        # Read the CSV file.
        df = pd.read_csv(file_path)

        # Display basic information.
        print("Dataset loaded successfully.")
        print(f"Path: {file_path}")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        return df

    except FileNotFoundError:

        # This error happens when the CSV file does not exist.
        print(
            f"Error: Dataset not found at:\n"
            f"{file_path}"
        )

        return None

    except Exception as error:

        # Handle any other unexpected error.
        print(
            f"Error while loading dataset: {error}"
        )

        return None


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    # Test the dataset loading function.
    load_data()