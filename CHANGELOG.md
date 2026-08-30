# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows semantic versioning principles where applicable.

---

## [Unreleased]

### Added

* Added a dedicated `data_loader.py` module for loading datasets.
* Added a dedicated `data_cleaning.py` module for data preprocessing.
* Added automatic creation of the `data/processed/` directory.
* Added cleaned dataset output:
  `AI_SocialMedia_Student_Health_Dataset_clean.csv`.
* Added data cleaning functions for:

  * Column name cleaning.
  * Text value cleaning.
  * Duplicate removal.
  * Numerical type conversion.
  * Missing value handling.
  * Numerical value validation.
  * Final dataset validation.
* Improved project documentation.
* Added project contribution guidelines.
* Added security guidelines.
* Added code of conduct.
* Added GitHub issue and pull request templates.

### Changed

* Separated dataset loading from data cleaning.
* Updated the project structure to separate raw and processed data.
* Improved code comments and documentation.
* Updated README to reflect the current project structure and workflow.

### Fixed

* Corrected the cleaned dataset output location.
* Removed duplicated dataset loading logic.
* Improved handling of missing numerical and categorical values.

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

Future releases will document:

* New analysis features.
* Data preprocessing improvements.
* Machine Learning models.
* Model evaluation results.
* New visualizations.
* Bug fixes.
* Documentation improvements.
