# ============================================================
# IMPORTS
# ============================================================

import os

import pandas as pd
import numpy as np

import matplotlib

# Use Matplotlib without opening GUI windows
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# PROJECT PATHS
# ============================================================

# Get the main project folder
PROJECT_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Folder where all charts will be saved
FIGURES_PATH = os.path.join(
    PROJECT_PATH,
    "reports",
    "figures"
)

# Create the folder if it does not exist
os.makedirs(FIGURES_PATH, exist_ok=True)


# ============================================================
# Function 1: Get Numerical Columns
# ============================================================

def get_numerical_columns(df):
    """
    Get all columns that contain numerical data.

    Example:
        Age
        Sleep_Hours
        Mental_Health_Score

    Args:
        df: A pandas DataFrame

    Returns:
        A list containing numerical column names
    """

    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns

    return list(numerical_columns)


# ============================================================
# Function 2: Get Categorical Columns
# ============================================================

def get_categorical_columns(df):
    """
    Get all columns that contain text or categories.

    Student_ID is excluded because it is an identifier,
    not a meaningful categorical variable.

    Example:
        Gender
        Education_Level
        Burnout_Level

    Args:
        df: A pandas DataFrame

    Returns:
        A list containing categorical column names
    """

    categorical_columns = df.select_dtypes(
        include=["object", "category"]
    ).columns

    # Remove Student_ID because every student has
    # a different ID and it is not useful for a count plot.
    categorical_columns = [
        column
        for column in categorical_columns
        if column != "Student_ID"
    ]

    return list(categorical_columns)


# ============================================================
# Function 3: Plot Correlation Heatmap
# ============================================================

def plot_correlation_heatmap(df):
    """
    Create a heatmap showing the correlation
    between numerical variables.
    """

    print("Creating correlation heatmap...")

    # Get numerical columns
    numbers = get_numerical_columns(df)

    # Calculate correlation
    correlation_table = df[numbers].corr()

    # Create the figure
    plt.figure(figsize=(12, 10))

    # Create heatmap
    sns.heatmap(
        correlation_table,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0
    )

    # Add title
    plt.title(
        "Correlation Between Numerical Variables"
    )

    plt.tight_layout()

    # File path
    file_path = os.path.join(
        FIGURES_PATH,
        "correlation_heatmap.png"
    )

    # Save the figure
    plt.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight"
    )

    # Close the figure
    plt.close()

    print(f"Saved: {file_path}")


# ============================================================
# Function 4: Plot Box Plots
# ============================================================

def plot_boxplots(df):
    """
    Create a box plot for every numerical column.

    Box plots help us identify:
        - Median
        - Quartiles
        - Data spread
        - Possible outliers
    """

    print("Creating box plots...")

    # Get numerical columns
    numbers = get_numerical_columns(df)

    # Create one box plot for each column
    for column in numbers:

        plt.figure(figsize=(8, 5))

        sns.boxplot(
            x=df[column]
        )

        plt.title(
            f"Box Plot of {column}"
        )

        plt.xlabel(column)

        plt.tight_layout()

        # File path
        file_path = os.path.join(
            FIGURES_PATH,
            f"boxplot_{column}.png"
        )

        # Save figure
        plt.savefig(
            file_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print(f"Saved: {file_path}")


# ============================================================
# Function 5: Plot Numerical Distributions
# ============================================================

def plot_numerical_distributions(df):
    """
    Create a histogram for every numerical column.

    Histograms help us understand how numerical
    data is distributed.
    """

    print("Creating histograms...")

    # Get numerical columns
    numbers = get_numerical_columns(df)

    # Create one histogram for each column
    for column in numbers:

        plt.figure(figsize=(8, 5))

        sns.histplot(
            data=df,
            x=column,
            kde=True
        )

        plt.title(
            f"Distribution of {column}"
        )

        plt.xlabel(column)

        plt.ylabel(
            "Number of Students"
        )

        plt.tight_layout()

        # File path
        file_path = os.path.join(
            FIGURES_PATH,
            f"distribution_{column}.png"
        )

        # Save figure
        plt.savefig(
            file_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print(f"Saved: {file_path}")


# ============================================================
# Function 6: Plot Categorical Distributions
# ============================================================

def plot_categorical_distributions(df):
    """
    Create a count plot for every categorical column.

    Count plots show how many records belong
    to each category.

    Columns with more than 20 unique categories
    are skipped to avoid creating unreadable plots.
    """

    print("Creating count plots...")

    # Get categorical columns
    categories = get_categorical_columns(df)

    # Create one count plot for each column
    for column in categories:

        # Count unique categories
        unique_values = df[column].nunique()

        print(
            f"Processing {column} "
            f"({unique_values} unique values)..."
        )

        # Skip columns with too many categories
        if unique_values > 20:

            print(
                f"Skipped {column}: "
                f"too many unique values."
            )

            continue

        plt.figure(figsize=(10, 6))

        sns.countplot(
            data=df,
            x=column
        )

        plt.title(
            f"Count Distribution of {column}"
        )

        plt.xlabel(column)

        plt.ylabel(
            "Number of Students"
        )

        # Rotate category names
        plt.xticks(
            rotation=45,
            ha="right"
        )

        plt.tight_layout()

        # File path
        file_path = os.path.join(
            FIGURES_PATH,
            f"countplot_{column}.png"
        )

        # Save figure
        plt.savefig(
            file_path,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

        print(f"Saved: {file_path}")


# ============================================================
# Function 7: Run All Visualizations
# ============================================================

def run_all_visualizations(df):
    """
    Run all visualization functions.

    This function creates:

        1. Correlation heatmap
        2. Box plots
        3. Numerical distributions
        4. Categorical distributions
    """

    print("\nStarting visualization process...")

    print("\nFigures will be saved in:")
    print(FIGURES_PATH)

    # --------------------------------------------------------
    # 1. Correlation Heatmap
    # --------------------------------------------------------

    plot_correlation_heatmap(df)

    # --------------------------------------------------------
    # 2. Box Plots
    # --------------------------------------------------------

    plot_boxplots(df)

    # --------------------------------------------------------
    # 3. Numerical Distributions
    # --------------------------------------------------------

    plot_numerical_distributions(df)

    # --------------------------------------------------------
    # 4. Categorical Distributions
    # --------------------------------------------------------

    plot_categorical_distributions(df)

    print("\nAll visualizations completed!")