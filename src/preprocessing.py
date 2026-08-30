# ============================================================
# PREPROCESSING
# ============================================================
#
# This file prepares the cleaned dataset for Machine Learning.
#
# Main responsibilities:
#
# 1. Load the cleaned dataset
# 2. Create useful engineered features
# 3. Separate features (X) from target (y)
# 4. Identify numerical and categorical columns
# 5. Build a preprocessing pipeline
# 6. Encode categorical features
# 7. Scale numerical features
#
# IMPORTANT:
# We do NOT fit the preprocessing steps on the whole dataset
# before splitting the data.
#
# The ML model should learn preprocessing parameters only
# from the training data.
#
# This helps prevent data leakage.
# ============================================================


# ============================================================
# IMPORTS
# ============================================================

# Import required libraries from the central imports file.

from src.imports import (
    pd,
    np,
    Pipeline,
    ColumnTransformer,
    StandardScaler,
    OneHotEncoder
)


# Import the processed dataset path from load_data.py.

from src.load_data import PROCESSED_DATA_PATH


# ============================================================
# PROJECT PATHS
# ============================================================

# PROCESSED_DATA_PATH points to:
#
# data/
# └── processed/
#     └── AI_SocialMedia_Student_Health_Dataset_clean.csv
#
# We can use this path instead of writing the full path again.


# Path where the fitted preprocessor can be saved later.

PREPROCESSOR_PATH = (
    PROCESSED_DATA_PATH.parent.parent
    / "models"
    / "preprocessor.pkl"
)


# ============================================================
# TARGET COLUMN
# ============================================================

# This is the column that we want the Machine Learning
# model to predict.
#
# 0 = No academic failure risk
# 1 = Academic failure risk

TARGET_COLUMN = "Academic_Failure_Risk"


# ============================================================
# LOAD CLEANED DATA
# ============================================================

def load_cleaned_data():
    """
    Load the cleaned dataset from the processed folder.

    Returns:
        pandas.DataFrame:
            The cleaned dataset.
    """

    print("\n" + "=" * 70)
    print("LOADING CLEANED DATASET")
    print("=" * 70)

    # Check if the cleaned dataset exists.

    if not PROCESSED_DATA_PATH.exists():

        raise FileNotFoundError(
            f"Cleaned dataset was not found:\n"
            f"{PROCESSED_DATA_PATH}"
        )

    # Read the cleaned CSV file.

    df = pd.read_csv(PROCESSED_DATA_PATH)

    # Display basic information.

    print("Dataset loaded successfully.")
    print(f"Path: {PROCESSED_DATA_PATH}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    return df


# ============================================================
# FEATURE ENGINEERING
# ============================================================

def create_engineered_features(df):
    """
    Create additional features for Machine Learning.

    The new features indicate whether a student:

    - Uses AI tools
    - Uses social media
    - Is physically active

    Returns:
        pandas.DataFrame:
            Dataset with the new features.
    """

    # Make a copy so the original DataFrame is not modified.

    df = df.copy()


    # --------------------------------------------------------
    # AI TOOL USER
    # --------------------------------------------------------

    # If Daily_AI_Tool_Usage_Hours is greater than 0,
    # the student uses AI tools.
    #
    # 0 = Does not use AI tools
    # 1 = Uses AI tools

    if "Daily_AI_Tool_Usage_Hours" in df.columns:

        df["Uses_AI_Tools"] = (
            df["Daily_AI_Tool_Usage_Hours"] > 0
        ).astype(int)


    # --------------------------------------------------------
    # SOCIAL MEDIA USER
    # --------------------------------------------------------

    # If Daily_Social_Media_Hours is greater than 0,
    # the student uses social media.
    #
    # 0 = Does not use social media
    # 1 = Uses social media

    if "Daily_Social_Media_Hours" in df.columns:

        df["Is_Social_Media_User"] = (
            df["Daily_Social_Media_Hours"] > 0
        ).astype(int)


    # --------------------------------------------------------
    # PHYSICALLY ACTIVE
    # --------------------------------------------------------

    # If Physical_Activity_Hours is greater than 0,
    # the student has some physical activity.
    #
    # 0 = No physical activity
    # 1 = Some physical activity

    if "Physical_Activity_Hours" in df.columns:

        df["Is_Physically_Active"] = (
            df["Physical_Activity_Hours"] > 0
        ).astype(int)


    # --------------------------------------------------------
    # DISPLAY CREATED FEATURES
    # --------------------------------------------------------

    print("\nEngineered features created:")

    engineered_columns = [
        "Uses_AI_Tools",
        "Is_Social_Media_User",
        "Is_Physically_Active"
    ]

    for column in engineered_columns:

        if column in df.columns:
            print(f"- {column}")


    return df


# ============================================================
# SEPARATE FEATURES AND TARGET
# ============================================================

def split_features_and_target(df):
    """
    Separate the dataset into:

    X = Input features
    y = Target variable

    Returns:
        X:
            Feature DataFrame

        y:
            Target Series
    """

    print("\n" + "=" * 70)
    print("SEPARATING FEATURES AND TARGET")
    print("=" * 70)


    # Make sure the target column exists.

    if TARGET_COLUMN not in df.columns:

        raise ValueError(
            f"Target column '{TARGET_COLUMN}' was not found."
        )


    # X contains all input features.

    X = df.drop(
        columns=[TARGET_COLUMN]
    )


    # y contains only the target.

    y = df[TARGET_COLUMN]


    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")


    return X, y


# ============================================================
# IDENTIFY COLUMN TYPES
# ============================================================

def identify_column_types(X):
    """
    Identify numerical and categorical columns.

    Numerical columns:
        Age, scores, hours, etc.

    Categorical columns:
        Gender, Education_Level, etc.

    Returns:
        numerical_columns
        categorical_columns
    """

    print("\n" + "=" * 70)
    print("IDENTIFYING COLUMN TYPES")
    print("=" * 70)


    # --------------------------------------------------------
    # NUMERICAL COLUMNS
    # --------------------------------------------------------

    numerical_columns = X.select_dtypes(
        include=np.number
    ).columns.tolist()


    # --------------------------------------------------------
    # CATEGORICAL COLUMNS
    # --------------------------------------------------------

    categorical_columns = X.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()


    # --------------------------------------------------------
    # DISPLAY NUMERICAL COLUMNS
    # --------------------------------------------------------

    print("\nNumerical columns:")

    for column in numerical_columns:
        print(f"- {column}")


    # --------------------------------------------------------
    # DISPLAY CATEGORICAL COLUMNS
    # --------------------------------------------------------

    print("\nCategorical columns:")

    for column in categorical_columns:
        print(f"- {column}")


    return numerical_columns, categorical_columns


# ============================================================
# BUILD PREPROCESSOR
# ============================================================

def build_preprocessor(
    numerical_columns,
    categorical_columns
):
    """
    Build the preprocessing pipeline.

    Numerical features:
        StandardScaler

    Categorical features:
        OneHotEncoder

    ColumnTransformer applies the correct preprocessing
    to each type of column.
    """

    print("\n" + "=" * 70)
    print("BUILDING PREPROCESSING PIPELINE")
    print("=" * 70)


    # --------------------------------------------------------
    # NUMERICAL PIPELINE
    # --------------------------------------------------------

    # StandardScaler changes numerical values so that
    # they are centered around 0 with a standard deviation
    # close to 1.

    numerical_pipeline = Pipeline(
        steps=[
            (
                "scaler",
                StandardScaler()
            )
        ]
    )


    # --------------------------------------------------------
    # CATEGORICAL PIPELINE
    # --------------------------------------------------------

    # Machine Learning models cannot directly work with
    # text categories.
    #
    # Example:
    #
    # Male
    # Female
    #
    # OneHotEncoder converts these categories into
    # numerical columns.

    categorical_pipeline = Pipeline(
        steps=[
            (
                "onehot",
                OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False
                )
            )
        ]
    )


    # --------------------------------------------------------
    # COMBINE BOTH PIPELINES
    # --------------------------------------------------------

    # ColumnTransformer sends numerical columns to the
    # numerical pipeline and categorical columns to the
    # categorical pipeline.

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numerical",
                numerical_pipeline,
                numerical_columns
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_columns
            )
        ]
    )


    print(
        "Preprocessing pipeline created successfully."
    )


    return preprocessor


# ============================================================
# MAIN PREPROCESSING FUNCTION
# ============================================================

def prepare_data():
    """
    Prepare the cleaned dataset for Machine Learning.

    Steps:

    1. Load cleaned dataset
    2. Create engineered features
    3. Separate X and y
    4. Identify column types
    5. Build preprocessing pipeline

    Returns:
        X
        y
        preprocessor
    """

    # --------------------------------------------------------
    # STEP 1: LOAD DATA
    # --------------------------------------------------------

    df = load_cleaned_data()


    # --------------------------------------------------------
    # STEP 2: FEATURE ENGINEERING
    # --------------------------------------------------------

    df = create_engineered_features(df)


    # --------------------------------------------------------
    # STEP 3: SPLIT X AND Y
    # --------------------------------------------------------

    X, y = split_features_and_target(df)


    # --------------------------------------------------------
    # STEP 4: IDENTIFY COLUMN TYPES
    # --------------------------------------------------------

    numerical_columns, categorical_columns = (
        identify_column_types(X)
    )


    # --------------------------------------------------------
    # STEP 5: BUILD PREPROCESSOR
    # --------------------------------------------------------

    preprocessor = build_preprocessor(
        numerical_columns,
        categorical_columns
    )


    # Return everything required by the ML stage.

    return X, y, preprocessor


# ============================================================
# TEST THE FILE
# ============================================================

# This code runs only when this file is executed directly.
#
# Example:
#
#     python -m src.preprocessing
#
# It will NOT run when the file is imported.

if __name__ == "__main__":

    X, y, preprocessor = prepare_data()


    print("\n" + "=" * 70)
    print("PREPROCESSING PREPARATION COMPLETED")
    print("=" * 70)


    print(f"\nFinal feature shape: {X.shape}")
    print(f"Target shape: {y.shape}")


    # --------------------------------------------------------
    # TARGET DISTRIBUTION
    # --------------------------------------------------------

    print("\nTarget distribution:")

    print(
        y.value_counts()
    )


    # --------------------------------------------------------
    # TARGET PERCENTAGES
    # --------------------------------------------------------

    print("\nTarget percentages:")

    print(
        (
            y.value_counts(normalize=True)
            * 100
        ).round(2)
    )


    print(
        "\nPreprocessor is ready for train/test processing."
    )