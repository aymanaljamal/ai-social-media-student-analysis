from src.imports import pd, np


def get_dataset_overview(df):
    """
    Display a complete overview of the dataset.
    """

    print("\n" + "=" * 80)
    print("DATASET OVERVIEW")
    print("=" * 80)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn Information:")
    print("-" * 80)

    for column in df.columns:
        print(
            f"{column:<35} "
            f"Type: {str(df[column].dtype):<12} "
            f"Non-Null: {df[column].notna().sum():<8} "
            f"Unique: {df[column].nunique()}"
        )


def get_column_types(df):
    """
    Display the type of every column.
    """

    print("\n" + "=" * 80)
    print("COLUMN TYPES")
    print("=" * 80)

    for column in df.columns:
        print(f"{column:<35} -> {df[column].dtype}")


def get_missing_values(df):
    """
    Analyze missing values.
    """

    print("\n" + "=" * 80)
    print("MISSING VALUES")
    print("=" * 80)

    missing = df.isnull().sum()
    missing_percentage = (missing / len(df)) * 100

    missing_table = pd.DataFrame({
        "Missing Values": missing,
        "Missing Percentage": missing_percentage
    })

    print(missing_table)

    print(
        f"\nTotal Missing Values: {missing.sum()}"
    )


def get_duplicate_values(df):
    """
    Check duplicated rows.
    """

    print("\n" + "=" * 80)
    print("DUPLICATES")
    print("=" * 80)

    duplicates = df.duplicated().sum()

    print(f"Duplicated Rows: {duplicates}")

    if duplicates == 0:
        print("No duplicated rows found.")


def get_numerical_statistics(df):
    """
    Calculate detailed statistics for numerical columns.
    """

    print("\n" + "=" * 80)
    print("NUMERICAL STATISTICS")
    print("=" * 80)

    numerical_df = df.select_dtypes(
        include=np.number
    )

    statistics = pd.DataFrame({
        "Count": numerical_df.count(),
        "Mean": numerical_df.mean(),
        "Median": numerical_df.median(),
        "Min": numerical_df.min(),
        "Max": numerical_df.max(),
        "Std": numerical_df.std(),
        "Variance": numerical_df.var(),
        "Q1": numerical_df.quantile(0.25),
        "Q2": numerical_df.quantile(0.50),
        "Q3": numerical_df.quantile(0.75),
        "IQR": (
            numerical_df.quantile(0.75)
            - numerical_df.quantile(0.25)
        ),
        "Skewness": numerical_df.skew(),
        "Kurtosis": numerical_df.kurtosis()
    })

    print(statistics.round(2))

    return statistics


def get_categorical_statistics(df):
    """
    Display statistics for categorical columns.
    """

    print("\n" + "=" * 80)
    print("CATEGORICAL STATISTICS")
    print("=" * 80)

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for column in categorical_columns:

        print(f"\n{column}")
        print("-" * 50)

        print(f"Data Type: {df[column].dtype}")
        print(f"Unique Values: {df[column].nunique()}")

        print("\nValue Counts:")
        print(df[column].value_counts())

        print("\nPercentage:")
        print(
            (df[column].value_counts(normalize=True) * 100)
            .round(2)
        )


def get_correlation(df):
    """
    Calculate correlation between numerical variables.
    """

    print("\n" + "=" * 80)
    print("CORRELATION MATRIX")
    print("=" * 80)

    numerical_df = df.select_dtypes(
        include=np.number
    )

    correlation = numerical_df.corr()

    print(correlation.round(2))

    return correlation


def get_target_distribution(df):
    """
    Analyze Academic Failure Risk.
    """

    target = "Academic_Failure_Risk"

    print("\n" + "=" * 80)
    print("TARGET VARIABLE")
    print("=" * 80)

    print(f"Target: {target}")

    print("\nCounts:")
    print(df[target].value_counts())

    print("\nPercentages:")
    print(
        (df[target].value_counts(normalize=True) * 100)
        .round(2)
    )


def run_basic_analysis(df):
    """
    Run the complete statistical analysis.
    """

    get_dataset_overview(df)

    get_column_types(df)

    get_missing_values(df)

    get_duplicate_values(df)

    get_numerical_statistics(df)

    get_categorical_statistics(df)

    get_correlation(df)

    get_target_distribution(df)