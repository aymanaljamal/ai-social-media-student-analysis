# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows semantic versioning principles where applicable.

---

## [1.0.0] - 2026-08-30

### Added

#### Data Analysis

* Added complete project structure for the student academic performance analysis project.
* Added dataset loading and validation.
* Added dataset inspection and overview.
* Added numerical feature analysis.
* Added categorical feature analysis.
* Added descriptive statistics.
* Added correlation analysis.
* Added data visualization.
* Added correlation heatmap.
* Added numerical distribution plots.
* Added box plots.
* Added categorical count plots.
* Added automatic figure generation and storage.

#### Data Preprocessing

* Added `preprocessing.py` for preparing cleaned data for Machine Learning.
* Added automatic identification of numerical and categorical features.
* Added numerical feature scaling using `StandardScaler`.
* Added categorical feature encoding using `OneHotEncoder`.
* Added a `ColumnTransformer` preprocessing pipeline.
* Added train/test splitting using an 80/20 split.
* Added stratified train/test splitting to preserve target class distribution.

#### Feature Engineering

Added derived features for:

* `Uses_AI_Tools`
* `Is_Social_Media_User`
* `Is_Physically_Active`

#### Machine Learning

* Added `train_model.py` for Machine Learning model training.
* Added Random Forest classification.
* Added class balancing to the Random Forest model.
* Added reproducible model training using `random_state=42`.
* Added automatic saving of the trained model.
* Added automatic saving of the fitted preprocessing pipeline.

#### Model Evaluation

Added evaluation using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

#### Generated Model Files

* `models/random_forest_model.pkl`
* `models/preprocessor.pkl`

---

### Changed

* Expanded the project workflow from initial Data Analysis to a complete Machine Learning pipeline.

* Updated the project workflow to include:

  1. Data Loading
  2. Data Cleaning
  3. Exploratory Data Analysis
  4. Data Visualization
  5. Data Preprocessing
  6. Feature Engineering
  7. Train/Test Split
  8. Model Training
  9. Model Evaluation
  10. Model Saving

* Updated project documentation to include Machine Learning results.

* Updated notebooks to document the complete analysis and Machine Learning workflow.

* Improved the organization of generated reports and figures.

* Updated the project status to reflect the completion of the Machine Learning stage.

---

### Machine Learning Results

The Random Forest model was trained on **12,000 records** and evaluated on **3,000 test records**.

| Metric            |     Result |
| ----------------- | ---------: |
| Accuracy          | **98.47%** |
| Class 0 Precision |   **0.99** |
| Class 0 Recall    |   **1.00** |
| Class 0 F1-score  |   **0.99** |
| Class 1 Precision |   **0.97** |
| Class 1 Recall    |   **0.77** |
| Class 1 F1-score  |   **0.86** |

### Confusion Matrix

```text
[[2816    4]
 [  42  138]]
```

---

### Fixed

* Prevented preprocessing data leakage by fitting the preprocessing pipeline only on training data.
* Ensured that test data is transformed without fitting preprocessing parameters again.
* Added reproducible train/test splitting using `random_state=42`.
* Added class balancing to the Random Forest model.
* Fixed project preprocessing and Machine Learning workflow issues.
* Improved model and preprocessing pipeline saving.
* Improved notebook execution and report generation workflow.

---

### Documentation

* Added documentation for the complete project workflow.
* Documented data analysis and visualization results.
* Documented preprocessing and feature engineering steps.
* Documented Machine Learning methodology.
* Documented model evaluation results.
* Added generated analysis reports and figures.
* Added notebook-based project reports.

---

### Project Status

**Version 1.0.0 — Completed**

The project now contains a complete end-to-end workflow for analyzing student academic performance and predicting academic failure risk using Machine Learning.

The implemented workflow covers:

**Data → Cleaning → Analysis → Visualization → Preprocessing → Feature Engineering → Machine Learning → Evaluation → Model Saving → Reporting**

---

## [0.1.0] - Initial Analysis

### Added

* Initial project structure.
* Dataset loading.
* Dataset inspection.
* Numerical analysis.
* Categorical analysis.
* Descriptive statistics.
* Correlation analysis.
* Data visualization.
* Correlation heatmap.
* Numerical distribution plots.
* Box plots.
* Categorical count plots.
* Automatic figure generation and storage.

### Project Scope

The initial version focuses on exploring relationships between:

* Social media usage.
* AI tool usage.
* Sleep.
* Physical activity.
* Mental health.
* Physical health.
* Social isolation.
* Burnout.
* Academic performance.
* Academic failure risk.

---

## Versioning

Future releases may include:

* Additional Machine Learning models.
* ROC-AUC analysis.
* Feature importance analysis.
* Hyperparameter tuning.
* Model comparison.
* Model performance improvements.
* New visualizations.
* Advanced statistical analysis.
* Prediction functionality.
* Bug fixes.
* Documentation improvements.
