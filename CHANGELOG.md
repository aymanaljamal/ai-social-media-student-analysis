# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows semantic versioning principles where applicable.

---

## [1.1.0] - 2026-09-01

### Added

#### Prediction System

* Added a complete student academic failure risk prediction workflow.
* Added `PredictionRequest` model for structured prediction input.
* Added `PredictionResult` model for structured prediction output.
* Added `PredictionService` for handling the prediction workflow.
* Added integration with the trained Random Forest model.
* Added integration with the fitted preprocessing pipeline.
* Added automatic loading of:

  * `models/random_forest_model.pkl`
  * `models/preprocessor.pkl`
* Added preprocessing and transformation of prediction input before inference.
* Added prediction of academic failure risk for individual students.
* Added prediction result classification.
* Added prediction confidence/probability information.
* Separated prediction logic from the user interface using a service-based architecture.

#### Prediction Input

Added structured prediction fields including:

* `Student_ID`
* `Age`
* `Gender`
* `Education_Level`
* `Daily_Social_Media_Hours`
* `Daily_AI_Tool_Usage_Hours`
* `Sleep_Hours`
* `Physical_Activity_Hours`
* `Mental_Health_Score`
* `Physical_Health_Score`
* `Social_Isolation_Score`
* `Burnout_Level`
* `Academic_Performance_Score`
* `Uses_AI_Tools`
* `Is_Social_Media_User`
* `Is_Physically_Active`

#### Prediction Cases

* Added JSON-based prediction cases for testing and demonstration.
* Added support for storing complete prediction inputs as JSON.
* Added reusable prediction cases that can be loaded directly by the application.
* Added generated student prediction scenarios.
* Added support for identifying high-risk student cases.
* Added command-line scripts for generating and analyzing prediction cases.

#### Desktop GUI

* Added a modern desktop GUI using `CustomTkinter`.
* Added a dedicated application main window.
* Added a Student Risk Prediction screen.
* Added a Prediction Result screen.
* Added an About / Project Information screen.
* Added navigation between application screens.
* Added separation between GUI, models, and business logic.
* Added a modern red-and-white visual design.
* Added reusable UI components and consistent styling.
* Added responsive layout configuration for the application interface.

#### Prediction Form Validation

* Added input validation for prediction fields.
* Added realistic limits for hour-based inputs.
* Added age validation.
* Added score validation using a `0–100` range.
* Added validation for:

  * Daily social media usage.
  * Daily AI tool usage.
  * Sleep hours.
  * Physical activity hours.
* Added clear validation messages.
* Added example values and input ranges to improve usability.
* Prevented unrealistic values from being submitted to the prediction system.

#### Application Structure

Added a structured application architecture separating responsibilities into:

* `models`
* `services`
* `ui`
* `scripts`
* `models` for trained ML artifacts
* prediction data / JSON resources
* configuration and application assets

The application now follows a clear flow:

**GUI → Prediction Request → Prediction Service → Preprocessor → Random Forest Model → Prediction Result → GUI**

#### Scripts

* Added scripts for generating prediction cases.
* Added scripts for finding high-risk prediction cases.
* Added reusable command-line prediction workflows.
* Improved script execution from the project root.
* Added project-root path handling to allow scripts to import application modules correctly.

---

### Changed

* Expanded the project from an offline Machine Learning workflow into an end-to-end prediction application.
* Updated the architecture to separate:

  * Data processing.
  * Machine Learning.
  * Prediction logic.
  * Application models.
  * User interface.
* Updated the prediction workflow to use the same fitted preprocessing pipeline used during model training.
* Updated the application to load the trained model and preprocessing pipeline instead of duplicating preprocessing logic.
* Improved prediction input organization using structured request models.
* Improved prediction output organization using structured result models.
* Updated the project UI to use a modern red-and-white theme.
* Improved form usability with clearer labels, examples, and validation ranges.
* Improved project organization according to a layered application structure.
* Updated documentation to include the prediction application architecture.
* Expanded testing and demonstration capabilities using reusable JSON prediction cases.
* Updated project status from Machine Learning completion to a complete prediction application stage.

---

### Fixed

* Fixed preprocessing consistency between model training and prediction.
* Prevented prediction-time preprocessing from being fitted again.
* Ensured the saved preprocessing pipeline is reused during inference.
* Fixed project-root import issues when executing scripts from the `scripts` directory.
* Improved handling of prediction input data.
* Improved validation of invalid and unrealistic user inputs.
* Improved separation between UI logic and prediction/business logic.
* Fixed inconsistencies in the prediction workflow.
* Improved model and preprocessing artifact loading.
* Improved error handling around prediction input validation.
* Improved execution of prediction-related scripts.

---

### User Interface

The application now provides a dedicated desktop interface containing:

1. **Main Window**

   * Application navigation.
   * Global layout.
   * Application branding.

2. **Student Risk Prediction**

   * Student information input.
   * Academic and lifestyle information.
   * Health and social indicators.
   * Input validation.
   * Prediction action.

3. **Prediction Result**

   * Predicted academic failure risk.
   * Prediction probability/confidence.
   * Result presentation.

4. **About**

   * Project information.
   * Machine Learning workflow.
   * Application information.

The interface follows a consistent **modern red-and-white design system**.

---

### Prediction Workflow

The application now supports the following complete workflow:

**Student Input**

↓

**Input Validation**

↓

**PredictionRequest**

↓

**PredictionService**

↓

**Saved Preprocessing Pipeline**

↓

**Random Forest Model**

↓

**Risk Prediction**

↓

**PredictionResult**

↓

**Results Screen**

---

### Machine Learning

The trained Random Forest model remains the primary prediction model.

Training configuration includes:

* Random Forest classification.
* Class balancing.
* Reproducible training using `random_state=42`.
* Saved preprocessing pipeline.
* Saved trained model.

Generated model artifacts:

* `models/random_forest_model.pkl`
* `models/preprocessor.pkl`

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

### Documentation

* Updated project documentation to cover the prediction application.
* Documented the prediction architecture.
* Documented prediction input fields.
* Documented prediction validation rules.
* Documented the model inference workflow.
* Documented the GUI structure.
* Documented prediction case generation and testing.
* Improved documentation of project structure.
* Updated project workflow documentation from Machine Learning to application-level prediction.

---

### Project Status

**Version 1.1.0 — Prediction Application Completed**

The project has evolved from a Data Analysis and Machine Learning project into a complete end-to-end student academic failure risk prediction application.

The implemented workflow now covers:

**Data → Cleaning → Analysis → Visualization → Preprocessing → Feature Engineering → Train/Test Split → Machine Learning → Evaluation → Model Saving → Prediction Service → Input Validation → Prediction → Result Presentation → Desktop GUI → Reporting**

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

The project contained a complete end-to-end workflow for analyzing student academic performance and predicting academic failure risk using Machine Learning.

The implemented workflow covered:

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

The initial version focused on exploring relationships between:

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
* Advanced prediction analytics.
* Prediction history.
* Batch prediction.
* Automated testing.
* GUI improvements.
* Bug fixes.
* Documentation improvements.
