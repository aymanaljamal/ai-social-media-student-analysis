# ============================================================
# EVALUATE MODEL
# ============================================================
#
# This file is responsible for evaluating the trained
# Machine Learning model.
#
# Main responsibilities:
#
# 1. Make predictions using the testing data
# 2. Calculate model accuracy
# 3. Display the classification report
# 4. Display the confusion matrix
#
# IMPORTANT:
# The model must already be trained before evaluation.
# ============================================================


# ============================================================
# IMPORTS
# ============================================================

# Import evaluation metrics from the central imports file.

from src.imports import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# EVALUATE MODEL
# ============================================================

def evaluate_model(
    model,
    X_test,
    y_test
):
    """
    Evaluate a trained Machine Learning model.

    Args:
        model:
            Trained Machine Learning model.

        X_test:
            Processed testing features.

        y_test:
            Real target values for the testing data.

    Returns:
        float:
            Model accuracy.
    """

    print("\n" + "=" * 70)
    print("EVALUATING MODEL")
    print("=" * 70)


    # --------------------------------------------------------
    # STEP 1: MAKE PREDICTIONS
    # --------------------------------------------------------

    # Ask the trained model to predict the target
    # for the testing data.

    y_pred = model.predict(
        X_test
    )


    # --------------------------------------------------------
    # STEP 2: CALCULATE ACCURACY
    # --------------------------------------------------------

    # Accuracy tells us how many predictions were correct.

    accuracy = accuracy_score(
        y_test,
        y_pred
    )


    print("\nAccuracy:")
    print(f"{accuracy:.4f}")


    # --------------------------------------------------------
    # STEP 3: CLASSIFICATION REPORT
    # --------------------------------------------------------

    # The classification report provides:
    #
    # Precision
    # Recall
    # F1-score
    # Support
    #
    # for each class.

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            y_pred
        )
    )


    # --------------------------------------------------------
    # STEP 4: CONFUSION MATRIX
    # --------------------------------------------------------

    # The confusion matrix shows:
    #
    # True Negatives
    # False Positives
    # False Negatives
    # True Positives

    print("\nConfusion Matrix:")

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    print(cm)


    # --------------------------------------------------------
    # RETURN ACCURACY
    # --------------------------------------------------------

    return accuracy


# ============================================================
# TEST THE FILE
# ============================================================

# This file is normally called from main.py.
#
# Therefore, there is no complete training process here.
#
# The function above receives an already trained model
# and evaluates it.