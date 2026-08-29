# ============================================================
# IMPORTS
# ============================================================

from src.load_data import load_data
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
    print("FIRST 5 ROWS")
    print("=" * 80)

    print(df.head())


    # --------------------------------------------------------
    # 4. Data Analysis
    # --------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("STARTING DATA ANALYSIS")
    print("=" * 80)

    run_basic_analysis(df)


    # --------------------------------------------------------
    # 5. Data Visualization
    # --------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("STARTING DATA VISUALIZATION")
    print("=" * 80)

    run_all_visualizations(df)


    # --------------------------------------------------------
    # 6. Finished
    # --------------------------------------------------------

    print("\n")
    print("=" * 80)
    print("PROJECT FINISHED")
    print("=" * 80)

    print("\nAll analysis and visualizations have been completed.")
    print("Charts were saved in: reports/figures/")


# ============================================================
# RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()