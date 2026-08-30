# ============================================================
# TRAIN MODEL
# ============================================================
#
# This file is responsible for training the Machine Learning
# model.
#
# Main responsibilities:
#
# 1. Prepare the dataset
# 2. Split the data into training and testing sets
# 3. Fit the preprocessing pipeline using training data only
# 4. Transform training and testing data
# 5. Create the Random Forest model
# 6. Train the model
# 7. Save the trained model
# 8. Save the fitted preprocessor
#
# IMPORTANT:
# The preprocessor is fitted only on the training data.
#
# This helps prevent data leakage.
# ============================================================


# ============================================================
# IMPORTS
# ============================================================

# Import required libraries from the central imports file.

from src.imports import (
    train_test_split,
    RandomForestClassifier
)


# Import the preprocessing function.

from src.preprocessing import prepare_data


# Import the processed dataset path.

from src.load_data import PROCESSED_DATA_PATH


# ============================================================
# PROJECT PATHS
# ============================================================

# PROCESSED_DATA_PATH points to:
#
# data/processed/
#     AI_SocialMedia_Student_Health_Dataset_clean.csv
#
# parent            -> processed
# parent.parent     -> data
# parent.parent.parent -> project root

MODELS_PATH = (
    PROCESSED_DATA_PATH.parent.parent.parent
    / "models"
)


# Path where the trained model will be saved.

MODEL_PATH = (
    MODELS_PATH
    / "random_forest_model.pkl"
)


# Path where the fitted preprocessor will be saved.

PREPROCESSOR_PATH = (
    MODELS_PATH
    / "preprocessor.pkl"
)


# ============================================================
# TRAINING SETTINGS
# ============================================================

# 20% of the dataset will be used for testing.

TEST_SIZE = 0.20


# random_state makes the split reproducible.

RANDOM_STATE = 42


# ============================================================
# PREPARE TRAINING DATA
# ============================================================

def prepare_training_data():
    """
    Prepare the dataset for Machine Learning training.

    Steps:

    1. Load and prepare the data.
    2. Split the data into training and testing sets.
    3. Fit the preprocessor using training data only.
    4. Transform training and testing data.

    Returns:
        X_train_processed:
            Processed training features.

        X_test_processed:
            Processed testing features.

        y_train:
            Training target values.

        y_test:
            Testing target values.

        preprocessor:
            Fitted preprocessing pipeline.
    """

    print("\n" + "=" * 70)
    print("PREPARING TRAINING DATA")
    print("=" * 70)


    # --------------------------------------------------------
    # STEP 1: PREPARE DATA
    # --------------------------------------------------------

    # prepare_data() returns:
    #
    # X            -> input features
    # y            -> target
    # preprocessor -> preprocessing pipeline

    X, y, preprocessor = prepare_data()


    # --------------------------------------------------------
    # STEP 2: TRAIN / TEST SPLIT
    # --------------------------------------------------------

    print("\nSplitting dataset into training and testing data...")


    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )


    # --------------------------------------------------------
    # DISPLAY SPLIT INFORMATION
    # --------------------------------------------------------

    print("\nTraining data:")
    print(f"X_train shape: {X_train.shape}")
    print(f"y_train shape: {y_train.shape}")


    print("\nTesting data:")
    print(f"X_test shape: {X_test.shape}")
    print(f"y_test shape: {y_test.shape}")


    # --------------------------------------------------------
    # STEP 3: FIT PREPROCESSOR
    # --------------------------------------------------------

    print(
        "\nFitting preprocessor on training data only..."
    )


    # IMPORTANT:
    #
    # fit_transform() is used only on X_train.
    #
    # The preprocessor learns scaling parameters and
    # categorical categories from the training data only.

    X_train_processed = preprocessor.fit_transform(
        X_train
    )


    # --------------------------------------------------------
    # STEP 4: TRANSFORM TEST DATA
    # --------------------------------------------------------

    print("Transforming testing data...")


    # IMPORTANT:
    #
    # We use transform() instead of fit_transform().
    #
    # This prevents the test data from influencing
    # the preprocessing process.

    X_test_processed = preprocessor.transform(
        X_test
    )


    # --------------------------------------------------------
    # DISPLAY PROCESSED DATA
    # --------------------------------------------------------

    print("\nProcessed training data:")
    print(
        f"X_train_processed shape: "
        f"{X_train_processed.shape}"
    )


    print("\nProcessed testing data:")
    print(
        f"X_test_processed shape: "
        f"{X_test_processed.shape}"
    )


    return (
        X_train_processed,
        X_test_processed,
        y_train,
        y_test,
        preprocessor
    )


# ============================================================
# CREATE RANDOM FOREST MODEL
# ============================================================

def create_random_forest_model():
    """
    Create the Random Forest classification model.

    Returns:
        RandomForestClassifier:
            A Random Forest classification model.
    """

    print("\n" + "=" * 70)
    print("CREATING RANDOM FOREST MODEL")
    print("=" * 70)


    # Create the Random Forest model.

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=RANDOM_STATE,
        class_weight="balanced"
    )


    print(
        "Random Forest model created successfully."
    )


    return model


# ============================================================
# TRAIN MODEL
# ============================================================

def train_model(
    model,
    X_train,
    y_train
):
    """
    Train the Machine Learning model.

    Args:
        model:
            Machine Learning model.

        X_train:
            Processed training features.

        y_train:
            Training target values.

    Returns:
        Trained Machine Learning model.
    """

    print("\n" + "=" * 70)
    print("TRAINING MODEL")
    print("=" * 70)


    # Train the model using training data.

    model.fit(
        X_train,
        y_train
    )


    print(
        "Model training completed successfully."
    )


    return model


# ============================================================
# SAVE MODEL AND PREPROCESSOR
# ============================================================

def save_model(
    model,
    preprocessor
):
    """
    Save the trained model and fitted preprocessor.

    Both files are saved inside the models folder.
    """

    print("\n" + "=" * 70)
    print("SAVING MODEL")
    print("=" * 70)


    # --------------------------------------------------------
    # CREATE MODELS DIRECTORY
    # --------------------------------------------------------

    # Create the models directory if it does not exist.

    MODELS_PATH.mkdir(
        parents=True,
        exist_ok=True
    )


    # --------------------------------------------------------
    # IMPORT JOBLIB
    # --------------------------------------------------------

    # joblib is commonly used to save scikit-learn models.

    import joblib


    # --------------------------------------------------------
    # SAVE TRAINED MODEL
    # --------------------------------------------------------

    joblib.dump(
        model,
        MODEL_PATH
    )


    # --------------------------------------------------------
    # SAVE PREPROCESSOR
    # --------------------------------------------------------

    joblib.dump(
        preprocessor,
        PREPROCESSOR_PATH
    )


    print("\nModel saved successfully:")
    print(MODEL_PATH)


    print("\nPreprocessor saved successfully:")
    print(PREPROCESSOR_PATH)


# ============================================================
# MAIN TRAINING FUNCTION
# ============================================================

def run_training():
    """
    Run the complete Machine Learning training process.

    Steps:

    1. Prepare training data.
    2. Create the Random Forest model.
    3. Train the model.
    4. Save the model and preprocessor.

    Returns:
        model:
            Trained Machine Learning model.

        preprocessor:
            Fitted preprocessing pipeline.

        X_test_processed:
            Processed testing features.

        y_test:
            Testing target values.
    """

    # --------------------------------------------------------
    # STEP 1: PREPARE DATA
    # --------------------------------------------------------

    (
        X_train_processed,
        X_test_processed,
        y_train,
        y_test,
        preprocessor
    ) = prepare_training_data()


    # --------------------------------------------------------
    # STEP 2: CREATE MODEL
    # --------------------------------------------------------

    model = create_random_forest_model()


    # --------------------------------------------------------
    # STEP 3: TRAIN MODEL
    # --------------------------------------------------------

    model = train_model(
        model,
        X_train_processed,
        y_train
    )


    # --------------------------------------------------------
    # STEP 4: SAVE MODEL
    # --------------------------------------------------------

    save_model(
        model,
        preprocessor
    )


    # --------------------------------------------------------
    # FINISHED
    # --------------------------------------------------------

    print("\n" + "=" * 70)
    print("MODEL TRAINING COMPLETED")
    print("=" * 70)


    return (
        model,
        preprocessor,
        X_test_processed,
        y_test
    )


# ============================================================
# TEST THE FILE
# ============================================================

# This code runs only when this file is executed directly.
#
# Example:
#
#     python -m src.train_model

if __name__ == "__main__":

    run_training()