
"""
============================================================
REPORT UTILITIES
============================================================

This module contains helper functions for saving and organizing
important outputs generated during the data analysis and
machine learning stages.

The module can save:

1. Figures and charts
2. Machine learning models
3. Evaluation metrics
4. Confusion matrices
5. Classification reports
6. Data tables
7. Jupyter notebooks as PDF files
8. JSON reports
9. Text reports

All generated files are stored inside the project's
"reports" directory.

Project structure:

data-analysis-project/
│
├── data/
├── notebooks/
├── utils/
│   └── report_utils.py
│
└── reports/
    ├── figures/
    ├── models/
    ├── metrics/
    ├── matrices/
    ├── notebooks/
    └── tables/

============================================================
"""


# ============================================================
# IMPORTS
# ============================================================

import asyncio
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ============================================================
# PROJECT PATHS
# ============================================================

# Get the directory where this Python file is located.
#
# Example:
# C:/Users/ayman/OneDrive/Desktop/data-analysis-project/utils
CURRENT_FILE_DIR = Path(__file__).resolve().parent

# The project root is one level above the "utils" directory.
#
# Example:
# C:/Users/ayman/OneDrive/Desktop/data-analysis-project
PROJECT_ROOT = CURRENT_FILE_DIR.parent

# Main reports directory.
REPORTS_DIR = PROJECT_ROOT / "reports"


# ============================================================
# REPORT SUBDIRECTORIES
# ============================================================

# Directory for charts and visualizations.
FIGURES_DIR = REPORTS_DIR / "figures"

# Directory for trained machine learning models.
MODELS_DIR = REPORTS_DIR / "models"

# Directory for evaluation metrics.
METRICS_DIR = REPORTS_DIR / "metrics"

# Directory for confusion matrices.
MATRICES_DIR = REPORTS_DIR / "matrices"

# Directory for CSV tables.
TABLES_DIR = REPORTS_DIR / "tables"

# Directory for notebook HTML/PDF files.
NOTEBOOKS_DIR = REPORTS_DIR / "notebooks"


# ============================================================
# CREATE REPORT DIRECTORIES
# ============================================================

def create_report_directories():
    """
    Create all required report directories.

    exist_ok=True means the function will not fail if
    the directories already exist.
    """

    directories = [
        REPORTS_DIR,
        FIGURES_DIR,
        MODELS_DIR,
        METRICS_DIR,
        MATRICES_DIR,
        TABLES_DIR,
        NOTEBOOKS_DIR,
    ]

    for directory in directories:
        directory.mkdir(
            parents=True,
            exist_ok=True
        )

    print("=" * 70)
    print("REPORT DIRECTORIES READY")
    print("=" * 70)
    print(f"Reports directory: {REPORTS_DIR}")
    print("=" * 70)


# Create the report directories automatically.
create_report_directories()


# ============================================================
# TIMESTAMP HELPER
# ============================================================

def get_timestamp():
    """
    Return the current date and time as a compact string.

    Example:
        20260830_151530
    """

    return datetime.now().strftime("%Y%m%d_%H%M%S")


# ============================================================
# SAVE FIGURE
# ============================================================

def save_figure(
    figure=None,
    filename="figure",
    dpi=300,
    close=True,
    subfolder=None
):
    """
    Save a Matplotlib figure inside reports/figures.

    Parameters
    ----------
    figure : matplotlib.figure.Figure, optional
        Figure object to save.

        If None, the current Matplotlib figure is used.

    filename : str
        Output filename without extension.

    dpi : int
        Image quality.

    close : bool
        Close the figure after saving.

    subfolder : str, optional
        Optional subfolder inside reports/figures.

    Returns
    -------
    Path
        Path of the saved image.
    """

    # Use the current figure if no figure was provided.
    if figure is None:
        figure = plt.gcf()

    # Create an optional subfolder.
    if subfolder:
        output_dir = FIGURES_DIR / subfolder
    else:
        output_dir = FIGURES_DIR

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    # Remove any existing extension.
    filename = Path(filename).stem

    # Final PNG path.
    output_path = output_dir / f"{filename}.png"

    # Save the figure.
    figure.savefig(
        output_path,
        dpi=dpi,
        bbox_inches="tight"
    )

    # Close the figure if requested.
    if close:
        plt.close(figure)

    print(f"Figure saved: {output_path}")

    return output_path


# ============================================================
# SAVE MULTIPLE FIGURES
# ============================================================

def save_all_figures(filename_prefix="figure"):
    """
    Save all currently open Matplotlib figures.

    Example:
        save_all_figures("analysis")
    """

    figure_numbers = plt.get_fignums()

    saved_files = []

    for index, figure_number in enumerate(
        figure_numbers,
        start=1
    ):

        figure = plt.figure(figure_number)

        filename = f"{filename_prefix}_{index}"

        path = save_figure(
            figure=figure,
            filename=filename,
            close=True
        )

        saved_files.append(path)

    print(f"\nSaved {len(saved_files)} figures.")

    return saved_files


# ============================================================
# SAVE MODEL
# ============================================================

def save_model(
    model,
    filename="model"
):
    """
    Save a trained machine learning model using joblib.

    Example:
        save_model(
            model,
            "academic_failure_model"
        )
    """

    filename = Path(filename).stem

    output_path = MODELS_DIR / f"{filename}.joblib"

    joblib.dump(
        model,
        output_path
    )

    print("=" * 70)
    print("MODEL SAVED")
    print("=" * 70)
    print(f"Model: {output_path}")
    print("=" * 70)

    return output_path


# ============================================================
# LOAD MODEL
# ============================================================

def load_model(filename):
    """
    Load a previously saved machine learning model.

    Example:
        model = load_model(
            "academic_failure_model"
        )
    """

    filename = Path(filename).stem

    model_path = MODELS_DIR / f"{filename}.joblib"

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )

    model = joblib.load(model_path)

    print(f"Model loaded: {model_path}")

    return model


# ============================================================
# SAVE METRICS
# ============================================================

def save_metrics(
    metrics,
    filename="model_metrics"
):
    """
    Save machine learning evaluation metrics.

    The function saves the metrics in:

    1. JSON
    2. CSV

    Example:

        metrics = {
            "accuracy": 0.91,
            "precision": 0.89,
            "recall": 0.87,
            "f1_score": 0.88
        }

        save_metrics(
            metrics,
            "model_metrics"
        )
    """

    filename = Path(filename).stem

    # --------------------------------------------------------
    # Save JSON
    # --------------------------------------------------------

    json_path = METRICS_DIR / f"{filename}.json"

    with open(
        json_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            metrics,
            file,
            indent=4,
            ensure_ascii=False,
            default=float
        )

    # --------------------------------------------------------
    # Save CSV
    # --------------------------------------------------------

    csv_path = METRICS_DIR / f"{filename}.csv"

    metrics_dataframe = pd.DataFrame(
        list(metrics.items()),
        columns=[
            "Metric",
            "Value"
        ]
    )

    metrics_dataframe.to_csv(
        csv_path,
        index=False,
        encoding="utf-8"
    )

    print("=" * 70)
    print("METRICS SAVED")
    print("=" * 70)
    print(f"JSON: {json_path}")
    print(f"CSV : {csv_path}")
    print("=" * 70)

    return {
        "json": json_path,
        "csv": csv_path
    }


# ============================================================
# SAVE CONFUSION MATRIX
# ============================================================

def save_confusion_matrix(
    matrix,
    filename="confusion_matrix",
    class_names=None
):
    """
    Save a confusion matrix as:

    1. PNG image
    2. CSV table
    3. NumPy file

    Parameters
    ----------
    matrix : array-like
        Confusion matrix.

    filename : str
        Output filename without extension.

    class_names : list, optional
        Names of the classes.
    """

    filename = Path(filename).stem

    # Convert input to NumPy array.
    matrix = np.asarray(matrix)

    # --------------------------------------------------------
    # Save CSV
    # --------------------------------------------------------

    csv_path = MATRICES_DIR / f"{filename}.csv"

    if class_names is not None:

        dataframe = pd.DataFrame(
            matrix,
            index=class_names,
            columns=class_names
        )

    else:

        dataframe = pd.DataFrame(matrix)

    dataframe.to_csv(
        csv_path,
        encoding="utf-8"
    )

    # --------------------------------------------------------
    # Save NumPy file
    # --------------------------------------------------------

    numpy_path = MATRICES_DIR / f"{filename}.npy"

    np.save(
        numpy_path,
        matrix
    )

    # --------------------------------------------------------
    # Create confusion matrix chart
    # --------------------------------------------------------

    figure, axis = plt.subplots(
        figsize=(7, 6)
    )

    image = axis.imshow(matrix)

    axis.set_title(
        "Confusion Matrix",
        fontsize=14,
        fontweight="bold"
    )

    axis.set_xlabel(
        "Predicted Label"
    )

    axis.set_ylabel(
        "Actual Label"
    )

    # Add class labels if provided.
    if class_names is not None:

        axis.set_xticks(
            range(len(class_names))
        )

        axis.set_yticks(
            range(len(class_names))
        )

        axis.set_xticklabels(
            class_names
        )

        axis.set_yticklabels(
            class_names
        )

    # Add numerical values inside the matrix.
    for row in range(matrix.shape[0]):

        for column in range(matrix.shape[1]):

            axis.text(
                column,
                row,
                str(matrix[row, column]),
                ha="center",
                va="center",
                fontsize=12
            )

    figure.colorbar(
        image,
        ax=axis
    )

    figure.tight_layout()

    # Save PNG.
    png_path = MATRICES_DIR / f"{filename}.png"

    figure.savefig(
        png_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(figure)

    print("=" * 70)
    print("CONFUSION MATRIX SAVED")
    print("=" * 70)
    print(f"PNG : {png_path}")
    print(f"CSV : {csv_path}")
    print(f"NPY : {numpy_path}")
    print("=" * 70)

    return {
        "png": png_path,
        "csv": csv_path,
        "npy": numpy_path
    }


# ============================================================
# SAVE CLASSIFICATION REPORT
# ============================================================

def save_classification_report(
    report,
    filename="classification_report"
):
    """
    Save a classification report as:

    1. JSON
    2. CSV

    The report is normally generated using:

        classification_report(
            y_true,
            y_pred,
            output_dict=True
        )
    """

    filename = Path(filename).stem

    # --------------------------------------------------------
    # Save JSON
    # --------------------------------------------------------

    json_path = METRICS_DIR / f"{filename}.json"

    with open(
        json_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4,
            ensure_ascii=False,
            default=float
        )

    # --------------------------------------------------------
    # Save CSV
    # --------------------------------------------------------

    csv_path = METRICS_DIR / f"{filename}.csv"

    dataframe = pd.DataFrame(
        report
    ).transpose()

    dataframe.to_csv(
        csv_path,
        encoding="utf-8"
    )

    print("=" * 70)
    print("CLASSIFICATION REPORT SAVED")
    print("=" * 70)
    print(f"JSON: {json_path}")
    print(f"CSV : {csv_path}")
    print("=" * 70)

    return {
        "json": json_path,
        "csv": csv_path
    }


# ============================================================
# SAVE DATAFRAME
# ============================================================

def save_dataframe(
    dataframe,
    filename="table"
):
    """
    Save a pandas DataFrame as CSV.

    Example:

        save_dataframe(
            df,
            "cleaned_dataset"
        )
    """

    filename = Path(filename).stem

    output_path = TABLES_DIR / f"{filename}.csv"

    dataframe.to_csv(
        output_path,
        index=False,
        encoding="utf-8"
    )

    print(f"Table saved: {output_path}")

    return output_path


# ============================================================
# SAVE FEATURE IMPORTANCE
# ============================================================

def save_feature_importance(
    feature_names,
    importance_values,
    filename="feature_importance"
):
    """
    Save feature importance values as:

    1. CSV
    2. PNG chart
    """

    filename = Path(filename).stem

    # Create DataFrame.
    dataframe = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importance_values
    })

    # Sort from most important to least important.
    dataframe = dataframe.sort_values(
        by="Importance",
        ascending=False
    )

    # --------------------------------------------------------
    # Save CSV
    # --------------------------------------------------------

    csv_path = TABLES_DIR / f"{filename}.csv"

    dataframe.to_csv(
        csv_path,
        index=False,
        encoding="utf-8"
    )

    # --------------------------------------------------------
    # Create chart
    # --------------------------------------------------------

    plot_dataframe = dataframe.head(20)

    figure, axis = plt.subplots(
        figsize=(10, 7)
    )

    axis.barh(
        plot_dataframe["Feature"],
        plot_dataframe["Importance"]
    )

    axis.set_title(
        "Feature Importance",
        fontsize=14,
        fontweight="bold"
    )

    axis.set_xlabel(
        "Importance"
    )

    axis.set_ylabel(
        "Feature"
    )

    axis.invert_yaxis()

    figure.tight_layout()

    # Save PNG.
    png_path = FIGURES_DIR / f"{filename}.png"

    figure.savefig(
        png_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(figure)

    print("=" * 70)
    print("FEATURE IMPORTANCE SAVED")
    print("=" * 70)
    print(f"CSV: {csv_path}")
    print(f"PNG: {png_path}")
    print("=" * 70)

    return {
        "csv": csv_path,
        "png": png_path
    }


# ============================================================
# SAVE TEXT REPORT
# ============================================================

def save_text_report(
    text,
    filename="report"
):
    """
    Save a text report.

    Useful for saving a readable summary of
    analysis or machine learning results.
    """

    filename = Path(filename).stem

    output_path = REPORTS_DIR / f"{filename}.txt"

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)

    print(f"Text report saved: {output_path}")

    return output_path


# ============================================================
# SAVE JSON REPORT
# ============================================================

def save_json_report(
    data,
    filename="report"
):
    """
    Save a dictionary-like report as JSON.
    """

    filename = Path(filename).stem

    output_path = REPORTS_DIR / f"{filename}.json"

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
            default=float
        )

    print(f"JSON report saved: {output_path}")

    return output_path


# ============================================================
# CONVERT NOTEBOOK TO PDF
# ============================================================

def notebook_to_pdf(
    notebook_path,
    output_name=None
):
    """
    Convert a Jupyter Notebook (.ipynb) to PDF.

    The notebook is first converted to HTML using nbconvert.

    Then Playwright + Chromium are used to convert the HTML
    file into a PDF.

    This method does not require Pandoc or LaTeX.

    Required packages:

        pip install playwright

    Then install Chromium:

        python -m playwright install chromium

    Parameters
    ----------
    notebook_path : str or Path
        Path to the Jupyter notebook.

    output_name : str, optional
        Name of the generated PDF.

    Returns
    -------
    Path or None
        Path of the generated PDF if successful.
        None if conversion fails.
    """

    # --------------------------------------------------------
    # Validate notebook path
    # --------------------------------------------------------

    notebook_path = Path(
        notebook_path
    )

    if not notebook_path.exists():

        raise FileNotFoundError(
            f"Notebook not found: {notebook_path}"
        )

    # --------------------------------------------------------
    # Determine output filename
    # --------------------------------------------------------

    if output_name is None:

        output_name = notebook_path.stem

    output_name = Path(
        output_name
    ).stem

    # --------------------------------------------------------
    # Make sure output directory exists
    # --------------------------------------------------------

    NOTEBOOKS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # Temporary HTML file.
    html_path = NOTEBOOKS_DIR / f"{output_name}.html"

    # Final PDF file.
    pdf_path = NOTEBOOKS_DIR / f"{output_name}.pdf"

    print()
    print("=" * 70)
    print("CONVERTING NOTEBOOK TO PDF")
    print("=" * 70)

    print(f"Notebook : {notebook_path}")
    print(f"Output   : {pdf_path}")

    # ========================================================
    # STEP 1 - Convert Notebook to HTML
    # ========================================================

    print()
    print("Step 1/2: Converting notebook to HTML...")

    html_command = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "html",
        str(notebook_path),
        "--output-dir",
        str(NOTEBOOKS_DIR),
        "--output",
        output_name
    ]

    try:

        result = subprocess.run(
            html_command,
            capture_output=True,
            text=True
        )

    except Exception as error:

        print()
        print("HTML conversion failed.")
        print(f"Error: {error}")

        return None

    # Check nbconvert result.
    if result.returncode != 0:

        print()
        print("HTML conversion failed.")

        if result.stderr:
            print(result.stderr)

        return None

    # Verify HTML file.
    if not html_path.exists():

        print()
        print(
            f"HTML file was not created: {html_path}"
        )

        return None

    print(
        f"HTML created successfully: {html_path}"
    )

    # ========================================================
    # STEP 2 - Convert HTML to PDF
    # ========================================================

    print()
    print(
        "Step 2/2: Converting HTML to PDF..."
    )

    # --------------------------------------------------------
    # Check Playwright before importing it.
    # --------------------------------------------------------

    try:

        from playwright.async_api import async_playwright

    except ImportError:

        print()
        print("PDF conversion failed.")
        print()
        print("Playwright is not installed.")
        print()
        print("Run this command inside your virtual environment:")
        print()
        print("    pip install playwright")
        print()
        print("Then install Chromium:")
        print()
        print("    python -m playwright install chromium")
        print()

        # Keep the HTML file because it can still be useful.
        print(
            f"HTML file was kept at:\n{html_path}"
        )

        return None

    # --------------------------------------------------------
    # Create PDF using Playwright.
    # --------------------------------------------------------

    async def create_pdf():

        async with async_playwright() as playwright:

            # Launch Chromium in headless mode.
            browser = await playwright.chromium.launch(
                headless=True
            )

            try:

                # Create a browser page.
                page = await browser.new_page(
                    viewport={
                        "width": 1600,
                        "height": 1000
                    }
                )

                # Convert Windows path to file URI.
                file_url = (
                    html_path
                    .resolve()
                    .as_uri()
                )

                # Open the generated HTML file.
                await page.goto(
                    file_url,
                    wait_until="networkidle"
                )

                # Give charts and images time to load.
                await page.wait_for_timeout(
                    2000
                )

                # Generate the PDF.
                await page.pdf(
                    path=str(pdf_path),
                    format="A4",
                    print_background=True,
                    margin={
                        "top": "15mm",
                        "bottom": "15mm",
                        "left": "12mm",
                        "right": "12mm"
                    }
                )

            finally:

                # Always close the browser.
                await browser.close()

    try:

        asyncio.run(
            create_pdf()
        )

    except Exception as error:

        print()
        print("PDF conversion failed.")
        print()
        print(f"Error: {error}")
        print()

        print(
            "If Chromium is not installed, run:"
        )

        print(
            "    python -m playwright install chromium"
        )

        print()

        # Keep HTML because PDF conversion failed.
        print(
            f"HTML file was kept at:\n{html_path}"
        )

        return None

    # --------------------------------------------------------
    # Verify PDF file.
    # --------------------------------------------------------

    if not pdf_path.exists():

        print()
        print(
            f"PDF file was not created: {pdf_path}"
        )

        return None

    # --------------------------------------------------------
    # Remove temporary HTML file.
    # --------------------------------------------------------

    try:

        html_path.unlink()

    except Exception:

        print(
            "Warning: Could not remove temporary "
            f"HTML file: {html_path}"
        )

    # ========================================================
    # SUCCESS
    # ========================================================

    print()
    print("=" * 70)
    print("NOTEBOOK CONVERTED SUCCESSFULLY")
    print("=" * 70)

    print(f"PDF: {pdf_path}")

    print("=" * 70)

    return pdf_path


# ============================================================
# CONVERT ALL NOTEBOOKS TO PDF
# ============================================================

def convert_all_notebooks_to_pdf(
    notebooks_directory=None
):
    """
    Convert all Jupyter notebooks in a directory to PDF.

    If no directory is provided, the function automatically
    uses the project's "notebooks" directory.

    Example:

        convert_all_notebooks_to_pdf()
    """

    # --------------------------------------------------------
    # Determine notebooks directory.
    # --------------------------------------------------------

    if notebooks_directory is None:

        notebooks_directory = (
            PROJECT_ROOT / "notebooks"
        )

    notebooks_directory = Path(
        notebooks_directory
    )

    # --------------------------------------------------------
    # Check directory.
    # --------------------------------------------------------

    if not notebooks_directory.exists():

        print(
            "Notebook directory not found: "
            f"{notebooks_directory}"
        )

        return []

    # --------------------------------------------------------
    # Find all notebooks.
    # --------------------------------------------------------

    notebook_files = sorted(
        notebooks_directory.glob("*.ipynb")
    )

    if not notebook_files:

        print(
            "No notebooks found in: "
            f"{notebooks_directory}"
        )

        return []

    # --------------------------------------------------------
    # Convert notebooks.
    # --------------------------------------------------------

    print("=" * 70)
    print("CONVERTING ALL NOTEBOOKS")
    print("=" * 70)

    converted_files = []

    for notebook in notebook_files:

        pdf_path = notebook_to_pdf(
            notebook
        )

        if pdf_path is not None:

            converted_files.append(
                pdf_path
            )

    # --------------------------------------------------------
    # Print summary.
    # --------------------------------------------------------

    print("=" * 70)
    print(
        f"Converted {len(converted_files)} "
        f"of {len(notebook_files)} notebooks."
    )
    print("=" * 70)

    return converted_files


# ============================================================
# SAVE COMPLETE MODEL REPORT
# ============================================================

def save_model_report(
    model,
    metrics=None,
    confusion_matrix=None,
    classification_report=None,
    model_name="model",
    class_names=None
):
    """
    Save all important machine learning outputs together.

    This function can save:

        - Model
        - Metrics
        - Confusion matrix
        - Classification report

    Example:

        save_model_report(
            model=model,
            metrics=metrics,
            confusion_matrix=cm,
            classification_report=report,
            model_name="academic_failure_model",
            class_names=[
                "Not At Risk",
                "At Risk"
            ]
        )
    """

    print("\n")
    print("=" * 80)
    print("SAVING COMPLETE MODEL REPORT")
    print("=" * 80)

    results = {}

    # --------------------------------------------------------
    # Save model.
    # --------------------------------------------------------

    if model is not None:

        results["model"] = save_model(
            model,
            model_name
        )

    # --------------------------------------------------------
    # Save metrics.
    # --------------------------------------------------------

    if metrics is not None:

        results["metrics"] = save_metrics(
            metrics,
            f"{model_name}_metrics"
        )

    # --------------------------------------------------------
    # Save confusion matrix.
    # --------------------------------------------------------

    if confusion_matrix is not None:

        results["confusion_matrix"] = (
            save_confusion_matrix(
                confusion_matrix,
                f"{model_name}_confusion_matrix",
                class_names
            )
        )

    # --------------------------------------------------------
    # Save classification report.
    # --------------------------------------------------------

    if classification_report is not None:

        results["classification_report"] = (
            save_classification_report(
                classification_report,
                f"{model_name}_classification_report"
            )
        )

    print("\n")
    print("=" * 80)
    print("MODEL REPORT COMPLETED")
    print("=" * 80)

    return results


# ============================================================
# SHOW REPORT STRUCTURE
# ============================================================

def show_report_structure():
    """
    Print the complete reports directory structure.
    """

    print("\n")
    print("=" * 80)
    print("REPORT DIRECTORY STRUCTURE")
    print("=" * 80)

    print(
        f"""
{REPORTS_DIR}/
│
├── figures/
│   └── Charts and visualizations
│
├── models/
│   └── Saved machine learning models
│
├── metrics/
│   └── Model evaluation metrics
│
├── matrices/
│   └── Confusion matrices and numerical matrices
│
├── tables/
│   └── CSV tables and feature importance
│
└── notebooks/
    └── Jupyter notebooks converted to PDF
"""
    )

    print("=" * 80)


# ============================================================
# MODULE TEST
# ============================================================

if __name__ == "__main__":

    print("\n")
    print("=" * 80)
    print("REPORT UTILITIES LOADED SUCCESSFULLY")
    print("=" * 80)

    print(
        f"Project root : {PROJECT_ROOT}"
    )

    print(
        f"Reports path : {REPORTS_DIR}"
    )

    show_report_structure()

    print()
    print("=" * 80)
    print("STARTING NOTEBOOK PDF CONVERSION")
    print("=" * 80)

    converted_files = (
        convert_all_notebooks_to_pdf()
    )

    print()
    print("=" * 80)
    print("PDF CONVERSION FINISHED")
    print("=" * 80)

    print(
        "Successfully converted: "
        f"{len(converted_files)} notebook(s)"
    )

    print()
    print(
        "You can now import this module "
        "from your notebooks."
    )
