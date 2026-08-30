# ============================================================
# IMPORTS
# ============================================================

from src.load_data import load_data
from src.data_cleaning import (
    clean_column_names,
    clean_text_values,
    remove_duplicates,
    convert_numeric_columns,
    handle_missing_values,
    validate_values,
    final_data_check,
    save_cleaned_data,
)
from src.data_analysis import run_basic_analysis
from src.visualization import run_all_visualizations


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    # --------------------------------------------------------
    # 1. Load Dataset
    # --------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("LOADING DATASET")
    print("=" * 80)

    df = load_data()


    # --------------------------------------------------------
    # 2. Check if Dataset Loaded Successfully
    # --------------------------------------------------------

    if df is None:
        print("\nDataset could not be loaded.")
        return


    # --------------------------------------------------------
    # 3. Display First 5 Rows
    # --------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("FIRST 5 ROWS - RAW DATA")
    print("=" * 80)

    print(df.head())


    # --------------------------------------------------------
    # 4. Data Cleaning
    # --------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("STARTING DATA CLEANING")
    print("=" * 80)

    # Clean column names.
    df = clean_column_names(df)

    # Clean text values.
    df = clean_text_values(df)

    # Remove duplicated rows.
    df = remove_duplicates(df)

    # Convert numerical columns to numeric data types.
    df = convert_numeric_columns(df)

    # Handle missing values.
    df = handle_missing_values(df)

    # Check for invalid numerical values.
    df = validate_values(df)

    # Perform a final check after cleaning.
    df = final_data_check(df)


    # --------------------------------------------------------
    # 5. Save Cleaned Dataset
    # --------------------------------------------------------

    save_cleaned_data(df)


    # --------------------------------------------------------
    # 6. Display Cleaned Data
    # --------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("FIRST 5 ROWS - CLEANED DATA")
    print("=" * 80)

    print(df.head())


    # --------------------------------------------------------
    # 7. Data Analysis
    # --------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("STARTING DATA ANALYSIS")
    print("=" * 80)

    run_basic_analysis(df)


    # --------------------------------------------------------
    # 8. Data Visualization
    # --------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("STARTING DATA VISUALIZATION")
    print("=" * 80)

    run_all_visualizations(df)


    # --------------------------------------------------------
    # 9. Finished
    # --------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("PROJECT FINISHED")
    print("=" * 80)

    print("\nAll analysis and visualizations have been completed.")
    print("Cleaned dataset was saved in: data/processed/")
    print("Charts were saved in: reports/figures/")


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()