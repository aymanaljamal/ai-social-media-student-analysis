# ============================================================
# TEST MACHINE LEARNING PIPELINE
# ============================================================
#
# This file tests the Machine Learning workflow using the
# already cleaned dataset.
#
# The workflow is:
#
# 1. Load the cleaned dataset
# 2. Create engineered features
# 3. Separate features and target
# 4. Split data into training and testing sets
# 5. Fit the preprocessing pipeline on training data
# 6. Transform training and testing data
# 7. Create the Random Forest model
# 8. Train the model
# 9. Evaluate the model
# 10. Display the final results
#
# This file does NOT load the raw dataset.
#
# Run from the project root:
#
#     python test.py
#
# ============================================================


# ============================================================
# IMPORTS
# ============================================================

# Import the complete training workflow.

from src.train_model import run_training


# Import the model evaluation function.

from src.evaluate_model import evaluate_model


# ============================================================
# MAIN TEST FUNCTION
# ============================================================

def main():

    # ========================================================
    # 1. START TEST
    # ========================================================

    print("\n")
    print("=" * 80)
    print("MACHINE LEARNING PIPELINE TEST")
    print("=" * 80)


    # ========================================================
    # 2. TRAIN MODEL
    # ========================================================

    print("\n")
    print("=" * 80)
    print("STARTING MODEL TRAINING")
    print("=" * 80)


    # run_training() handles:
    #
    # - Loading the cleaned dataset
    # - Feature engineering
    # - Separating X and y
    # - Train/test split
    # - Preprocessing
    # - Creating Random Forest
    # - Training the model
    # - Saving the model
    # - Saving the preprocessor

    (
        model,
        preprocessor,
        X_test_processed,
        y_test
    ) = run_training()


    # ========================================================
    # 3. EVALUATE MODEL
    # ========================================================

    print("\n")
    print("=" * 80)
    print("STARTING MODEL EVALUATION")
    print("=" * 80)


    # evaluate_model() handles:
    #
    # - Making predictions
    # - Calculating accuracy
    # - Classification report
    # - Confusion matrix

    accuracy = evaluate_model(
        model,
        X_test_processed,
        y_test
    )


    # ========================================================
    # 4. FINAL RESULTS
    # ========================================================

    print("\n")
    print("=" * 80)
    print("FINAL TEST RESULTS")
    print("=" * 80)


    # Display the final accuracy.

    print(
        f"\nModel Accuracy: {accuracy:.4f}"
    )


    print(
        f"Model Accuracy Percentage: "
        f"{accuracy * 100:.2f}%"
    )


    # ========================================================
    # 5. PROJECT FILES
    # ========================================================

    print("\nGenerated model files:")

    print(
        "models/random_forest_model.pkl"
    )

    print(
        "models/preprocessor.pkl"
    )


    # ========================================================
    # 6. SUCCESS MESSAGE
    # ========================================================

    print("\n")
    print("=" * 80)
    print("MACHINE LEARNING TEST COMPLETED")
    print("=" * 80)


    print(
        "\nThe model was trained and evaluated successfully."
    )


# ============================================================
# RUN TEST
# ============================================================

# This section runs only when test.py is executed directly.

if __name__ == "__main__":

    main()