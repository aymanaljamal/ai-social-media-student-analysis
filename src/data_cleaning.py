
"""
data_cleaning.py

This file contains simple and clear functions for cleaning
the AI & Social Media Student Health dataset.

The cleaning process includes:

1. Clean column names.
2. Clean text values.
3. Remove duplicate rows.
4. Convert numerical columns.
5. Handle missing values.
6. Check for invalid values.
7. Perform a final data check.
8. Save the cleaned dataset.

The code is intentionally written in a beginner-friendly way.
"""

# ============================================================
# IMPORTS
# ============================================================

from src.imports import pd, np

from src.data_loader import (
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

    cleaned_columns = []

    # Loop through every column name.
    for column in df.columns:

        # Convert the column name to text.
        column = str(column)

        # Remove spaces from the beginning and end.
        column = column.strip()

        # Replace spaces with underscores.
        column = column.replace(" ", "_")

        cleaned_columns.append(column)

    # Replace the old column names.
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

        " Male " -> "Male"
        " Female " -> "Female"
    """

    print("\nCleaning text values...")

    # Find columns that contain text data.
    text_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    # Clean every text column.
    for column in text_columns:

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
    Convert columns that should contain numbers into numeric
    data types.

    Invalid values are converted to NaN.
    """

    print("\nChecking numerical columns...")

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

    # Process each numerical column.
    for column in numerical_columns:

        # Only process the column if it exists.
        if column in df.columns:

            # Convert values to numbers.
            #
            # If a value cannot be converted,
            # pandas changes it to NaN.
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
    Handle missing values.

    Numerical columns:
        Missing values are replaced with the median.

    Categorical columns:
        Missing values are replaced with the most common value.
    """

    print("\nChecking missing values...")

    # Count missing values before cleaning.
    missing_before = df.isnull().sum().sum()

    print(f"Missing values before cleaning: {missing_before}")


    # --------------------------------------------------------
    # NUMERICAL COLUMNS
    # --------------------------------------------------------

    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns

    for column in numerical_columns:

        # Check if the column contains missing values.
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

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for column in categorical_columns:

        # Check if the column contains missing values.
        if df[column].isnull().any():

            # Find the most common value.
            most_common_value = df[column].mode()[0]

            # Replace missing values.
            df[column] = df[column].fillna(
                most_common_value
            )

            print(
                f"Filled missing values in {column} "
                f"with: {most_common_value}"
            )


    # Count missing values after cleaning.
    missing_after = df.isnull().sum().sum()

    print(f"Missing values after cleaning: {missing_after}")

    return df


# ============================================================
# FUNCTION 6: VALIDATE VALUES
# ============================================================

def validate_values(df):
    """
    Check important numerical columns for impossible values.

    This function does not delete invalid values.

    It only reports them so we can decide what to do with them.
    """

    print("\n" + "=" * 70)
    print("VALIDATING NUMERICAL VALUES")
    print("=" * 70)

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

    # Check every expected numerical column.
    for column, (minimum, maximum) in expected_ranges.items():

        # Skip the column if it does not exist.
        if column not in df.columns:
            continue

        # Find values outside the expected range.
        invalid_values = df[
            (df[column] < minimum)
            | (df[column] > maximum)
        ]

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
    """

    print("\n" + "=" * 70)
    print("FINAL DATA CHECK")
    print("=" * 70)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print(
        f"Missing values: "
        f"{df.isnull().sum().sum()}"
    )

    print(
        f"Duplicate rows: "
        f"{df.duplicated().sum()}"
    )

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

    # Save the cleaned dataset.
    df.to_csv(
        output_path,
        index=False
    )

    print("Cleaned dataset saved successfully.")
    print(f"Path: {output_path}")

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
        4. Remove duplicates.
        5. Convert numerical columns.
        6. Handle missing values.
        7. Validate values.
        8. Perform final data check.
        9. Save cleaned data.
    """

    print("\n" + "=" * 70)
    print("STARTING DATA CLEANING")
    print("=" * 70)


    # --------------------------------------------------------
    # STEP 1: LOAD DATA
    # --------------------------------------------------------

    df = load_data()

    # Stop if the dataset could not be loaded.
    if df is None:
        return None


    # --------------------------------------------------------
    # STEP 2: CLEAN COLUMN NAMES
    # --------------------------------------------------------

    df = clean_column_names(df)


    # --------------------------------------------------------
    # STEP 3: CLEAN TEXT VALUES
    # --------------------------------------------------------

    df = clean_text_values(df)


    # --------------------------------------------------------
    # STEP 4: REMOVE DUPLICATES
    # --------------------------------------------------------

    df = remove_duplicates(df)


    # --------------------------------------------------------
    # STEP 5: CONVERT NUMERICAL COLUMNS
    # --------------------------------------------------------

    df = convert_numeric_columns(df)


    # --------------------------------------------------------
    # STEP 6: HANDLE MISSING VALUES
    # --------------------------------------------------------

    df = handle_missing_values(df)


    # --------------------------------------------------------
    # STEP 7: VALIDATE VALUES
    # --------------------------------------------------------

    df = validate_values(df)


    # --------------------------------------------------------
    # STEP 8: FINAL CHECK
    # --------------------------------------------------------

    df = final_data_check(df)


    # --------------------------------------------------------
    # STEP 9: SAVE CLEANED DATA
    # --------------------------------------------------------

    save_cleaned_data(df)


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
