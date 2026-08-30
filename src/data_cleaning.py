
"""
data_cleaning.py

This file contains simple and clear functions for cleaning
the AI & Social Media Student Health dataset.

The cleaning process includes:

1. Load the raw dataset.
2. Clean column names.
3. Clean text values.
4. Remove duplicate rows.
5. Convert numerical columns.
6. Handle missing values.
7. Check for invalid values.
8. Perform a final data check.
9. Save the cleaned dataset.

The code is intentionally written in a beginner-friendly way.
"""


# ============================================================
# IMPORTS
# ============================================================

import pandas as pd
import numpy as np

from src.load_data import (
    load_data,
    PROCESSED_DATA_PATH
)


# ============================================================
# FUNCTION 1: CLEAN COLUMN NAMES
# ============================================================

def clean_column_names(df):
    """
    Clean the names of all columns.

    We:
    - Remove spaces from the beginning and end.
    - Replace spaces with underscores.

    Example:

        "Academic Performance Score"

    becomes:

        "Academic_Performance_Score"
    """

    print("\nCleaning column names...")

    # Create an empty list to store the cleaned column names.
    cleaned_columns = []

    # Loop through every column name.
    for column in df.columns:

        # Make sure the column name is treated as text.
        column = str(column)

        # Remove spaces from the beginning and end.
        column = column.strip()

        # Replace spaces with underscores.
        column = column.replace(" ", "_")

        # Add the cleaned column name to the list.
        cleaned_columns.append(column)

    # Replace the old column names with the cleaned names.
    df.columns = cleaned_columns

    print("Column names cleaned.")

    return df


# ============================================================
# FUNCTION 2: CLEAN TEXT VALUES
# ============================================================

def clean_text_values(df):
    """
    Remove unnecessary spaces from text values.

    Example:

        " Male "   -> "Male"
        " Female " -> "Female"
    """

    print("\nCleaning text values...")

    # Find columns that contain text or category data.
    text_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    # Loop through every text column.
    for column in text_columns:

        # Remove spaces from text values.
        #
        # Missing values are kept unchanged.
        df[column] = df[column].apply(
            lambda value: value.strip()
            if isinstance(value, str)
            else value
        )

    print("Text values cleaned.")

    return df


# ============================================================
# FUNCTION 3: REMOVE DUPLICATES
# ============================================================

def remove_duplicates(df):
    """
    Remove completely duplicated rows.

    Duplicate rows can affect the accuracy of our analysis.
    """

    print("\nChecking for duplicate rows...")

    # Count duplicated rows before removing them.
    duplicate_count = df.duplicated().sum()

    print(f"Duplicated rows found: {duplicate_count}")

    # Remove duplicated rows.
    df = df.drop_duplicates()

    print(f"Rows after removing duplicates: {len(df)}")

    return df


# ============================================================
# FUNCTION 4: CONVERT NUMERICAL COLUMNS
# ============================================================

def convert_numeric_columns(df):
    """
    Convert columns that should contain numbers
    into numeric data types.

    If a value cannot be converted to a number,
    pandas changes it to NaN.

    NaN represents a missing value.
    """

    print("\nChecking numerical columns...")

    # List of columns that should contain numerical values.
    numerical_columns = [

        "Age",

        "Daily_Social_Media_Hours",

        "Daily_AI_Tool_Usage_Hours",

        "Sleep_Hours",

        "Physical_Activity_Hours",

        "Mental_Health_Score",

        "Physical_Health_Score",

        "Academic_Performance_Score",

        "Social_Isolation_Score",

        "Academic_Failure_Risk",
    ]

    # Loop through every expected numerical column.
    for column in numerical_columns:

        # Only process the column if it exists in the dataset.
        if column in df.columns:

            # Convert the column values to numbers.
            #
            # Invalid values become NaN.
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

            print(f"Converted to numeric: {column}")

    return df


# ============================================================
# FUNCTION 5: HANDLE MISSING VALUES
# ============================================================

def handle_missing_values(df):
    """
    Handle missing values in the dataset.

    For numerical columns:
        Missing values are replaced with the median.

    For categorical columns:
        Missing values are replaced with the most common value.
    """

    print("\nChecking missing values...")

    # Count all missing values before cleaning.
    missing_before = df.isnull().sum().sum()

    print(
        f"Missing values before cleaning: "
        f"{missing_before}"
    )


    # --------------------------------------------------------
    # NUMERICAL COLUMNS
    # --------------------------------------------------------

    # Find all numerical columns.
    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns

    # Loop through numerical columns.
    for column in numerical_columns:

        # Check if this column contains missing values.
        if df[column].isnull().any():

            # Calculate the median value.
            median_value = df[column].median()

            # Replace missing values with the median.
            df[column] = df[column].fillna(
                median_value
            )

            print(
                f"Filled missing values in {column} "
                f"with median: {median_value:.2f}"
            )


    # --------------------------------------------------------
    # CATEGORICAL COLUMNS
    # --------------------------------------------------------

    # Find all text/categorical columns.
    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    # Loop through categorical columns.
    for column in categorical_columns:

        # Check if this column contains missing values.
        if df[column].isnull().any():

            # Find the most common value.
            most_common_value = df[column].mode()[0]

            # Replace missing values with the most common value.
            df[column] = df[column].fillna(
                most_common_value
            )

            print(
                f"Filled missing values in {column} "
                f"with: {most_common_value}"
            )


    # --------------------------------------------------------
    # CHECK MISSING VALUES AFTER CLEANING
    # --------------------------------------------------------

    # Count missing values after cleaning.
    missing_after = df.isnull().sum().sum()

    print(
        f"Missing values after cleaning: "
        f"{missing_after}"
    )

    return df


# ============================================================
# FUNCTION 6: VALIDATE VALUES
# ============================================================

def validate_values(df):
    """
    Check important numerical columns for impossible values.

    This function does not delete invalid values.

    It only reports them so we can decide what to do later.
    """

    print("\n" + "=" * 70)
    print("VALIDATING NUMERICAL VALUES")
    print("=" * 70)

    # Define the expected minimum and maximum
    # values for important numerical columns.
    expected_ranges = {

        "Age": (0, 120),

        "Daily_Social_Media_Hours": (0, 24),

        "Daily_AI_Tool_Usage_Hours": (0, 24),

        "Sleep_Hours": (0, 24),

        "Physical_Activity_Hours": (0, 24),

        "Mental_Health_Score": (0, 100),

        "Physical_Health_Score": (0, 100),

        "Academic_Performance_Score": (0, 100),

        "Social_Isolation_Score": (0, 100),

        "Academic_Failure_Risk": (0, 1),
    }

    # Loop through every column and its expected range.
    for column, (minimum, maximum) in expected_ranges.items():

        # Skip the column if it does not exist.
        if column not in df.columns:
            continue

        # Find values below the minimum
        # or above the maximum.
        invalid_values = df[
            (df[column] < minimum)
            | (df[column] > maximum)
        ]

        # Display the number of invalid values.
        print(
            f"{column:<35} "
            f"Invalid values: {len(invalid_values)}"
        )

    return df


# ============================================================
# FUNCTION 7: FINAL DATA CHECK
# ============================================================

def final_data_check(df):
    """
    Display a final summary of the cleaned dataset.

    This allows us to make sure the cleaning process
    completed successfully.
    """

    print("\n" + "=" * 70)
    print("FINAL DATA CHECK")
    print("=" * 70)

    # Display number of rows.
    print(f"Rows: {df.shape[0]}")

    # Display number of columns.
    print(f"Columns: {df.shape[1]}")

    # Display the total number of missing values.
    print(
        f"Missing values: "
        f"{df.isnull().sum().sum()}"
    )

    # Display the total number of duplicate rows.
    print(
        f"Duplicate rows: "
        f"{df.duplicated().sum()}"
    )

    # Display the data types of all columns.
    print("\nData types:")
    print(df.dtypes)

    return df


# ============================================================
# FUNCTION 8: SAVE CLEANED DATA
# ============================================================

def save_cleaned_data(
    df,
    output_path=PROCESSED_DATA_PATH
):
    """
    Save the cleaned DataFrame as a CSV file.

    The processed folder is created automatically
    if it does not already exist.
    """

    print("\n" + "=" * 70)
    print("SAVING CLEANED DATA")
    print("=" * 70)

    # Create the output folder if it does not exist.
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save the cleaned DataFrame.
    #
    # index=False prevents pandas from creating
    # an extra index column in the CSV file.
    df.to_csv(
        output_path,
        index=False
    )

    print("Cleaned dataset saved successfully.")

    print(
        f"Path: {output_path}"
    )

    return output_path


# ============================================================
# FUNCTION 9: RUN COMPLETE CLEANING PROCESS
# ============================================================

def clean_dataset():
    """
    Run the complete data cleaning process.

    Steps:

        1. Load raw data.
        2. Clean column names.
        3. Clean text values.
        4. Remove duplicate rows.
        5. Convert numerical columns.
        6. Handle missing values.
        7. Validate numerical values.
        8. Perform a final data check.
        9. Save the cleaned dataset.

    Returns:
        pandas.DataFrame:
        The cleaned dataset.
    """

    print("\n" + "=" * 70)
    print("STARTING DATA CLEANING")
    print("=" * 70)


    # --------------------------------------------------------
    # STEP 1: LOAD DATA
    # --------------------------------------------------------

    print("\nSTEP 1: Loading dataset...")

    df = load_data()

    # Stop the process if the dataset could not be loaded.
    if df is None:

        print(
            "\nData cleaning stopped because "
            "the dataset could not be loaded."
        )

        return None


    # --------------------------------------------------------
    # STEP 2: CLEAN COLUMN NAMES
    # --------------------------------------------------------

    print("\nSTEP 2: Cleaning column names...")

    df = clean_column_names(df)


    # --------------------------------------------------------
    # STEP 3: CLEAN TEXT VALUES
    # --------------------------------------------------------

    print("\nSTEP 3: Cleaning text values...")

    df = clean_text_values(df)


    # --------------------------------------------------------
    # STEP 4: REMOVE DUPLICATES
    # --------------------------------------------------------

    print("\nSTEP 4: Removing duplicate rows...")

    df = remove_duplicates(df)


    # --------------------------------------------------------
    # STEP 5: CONVERT NUMERICAL COLUMNS
    # --------------------------------------------------------

    print("\nSTEP 5: Converting numerical columns...")

    df = convert_numeric_columns(df)


    # --------------------------------------------------------
    # STEP 6: HANDLE MISSING VALUES
    # --------------------------------------------------------

    print("\nSTEP 6: Handling missing values...")

    df = handle_missing_values(df)


    # --------------------------------------------------------
    # STEP 7: VALIDATE VALUES
    # --------------------------------------------------------

    print("\nSTEP 7: Validating numerical values...")

    df = validate_values(df)


    # --------------------------------------------------------
    # STEP 8: FINAL DATA CHECK
    # --------------------------------------------------------

    print("\nSTEP 8: Performing final data check...")

    df = final_data_check(df)


    # --------------------------------------------------------
    # STEP 9: SAVE CLEANED DATA
    # --------------------------------------------------------

    print("\nSTEP 9: Saving cleaned dataset...")

    save_cleaned_data(df)


    # --------------------------------------------------------
    # FINISHED
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("DATA CLEANING COMPLETED")
    print("=" * 70)

    return df


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    # Run the complete cleaning process.
    clean_dataset()
