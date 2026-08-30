# Project Documentation

# AI & Social Media Impact on Student Health & Academic Performance

## 1. Introduction

This project analyzes the relationship between students' digital behavior, health indicators, social factors, burnout, and academic performance.

The project uses Python-based Data Science tools to perform:

* Data loading.
* Data cleaning.
* Exploratory Data Analysis.
* Statistical analysis.
* Data visualization.
* Correlation analysis.
* Data preprocessing.
* Machine Learning.

The project is designed as an educational and practical Data Science project.

---

# 2. Dataset

The project uses the:

**AI & Social Media Impact: Student Health & Grades**

dataset.

The dataset contains approximately:

* 15,000 student records.
* 14 variables.

The variables represent demographic information, digital behavior, health indicators, social factors, burnout, academic performance, and academic failure risk.

---

# 3. Data Pipeline

The project follows this general workflow:

```text
Raw Dataset
     |
     v
Data Loading
     |
     v
Data Inspection
     |
     v
Data Cleaning
     |
     v
Processed Dataset
     |
     v
Exploratory Data Analysis
     |
     v
Statistical Analysis
     |
     v
Visualization
     |
     v
Feature Engineering
     |
     v
Machine Learning
     |
     v
Model Evaluation
```

---

# 4. Project Modules

## `src/imports.py`

Contains shared Python library imports used by the project.

Main libraries include:

* Pandas.
* NumPy.
* Matplotlib.
* Seaborn.
* Scikit-learn.

---

## `src/data_loader.py`

Responsible for loading datasets.

Main function:

```python
load_data()
```

The default input is:

```text
data/raw/AI_SocialMedia_Student_Health_Dataset.csv
```

---

## `src/data_cleaning.py`

Responsible for preparing the dataset for further analysis.

Main functions include:

```python
clean_column_names()
clean_text_values()
remove_duplicates()
convert_numeric_columns()
handle_missing_values()
validate_values()
final_data_check()
save_cleaned_data()
clean_dataset()
```

---

# 5. Data Cleaning Process

## Column Names

Column names are standardized by:

* Removing unnecessary spaces.
* Replacing spaces with underscores.

Example:

```text
Academic Performance Score
```

becomes:

```text
Academic_Performance_Score
```

---

## Text Values

Unnecessary spaces are removed from categorical values.

Example:

```text
" Male "
```

becomes:

```text
"Male"
```

---

## Duplicate Records

Completely duplicated rows are identified and removed.

---

## Numerical Data

Expected numerical columns are converted using:

```python
pd.to_numeric()
```

Invalid numerical values are converted to:

```text
NaN
```

---

## Missing Values

Numerical missing values are replaced using the median.

Categorical missing values are replaced using the most common category.

---

## Value Validation

Important numerical variables are checked against expected ranges.

Examples:

```text
Age: 0 - 120
Sleep_Hours: 0 - 24
Mental_Health_Score: 0 - 100
Academic_Performance_Score: 0 - 100
Academic_Failure_Risk: 0 - 1
```

The validation step reports suspicious values instead of automatically deleting them.

---

# 6. Output Dataset

The cleaned dataset is saved to:

```text
data/processed/
```

with the filename:

```text
AI_SocialMedia_Student_Health_Dataset_clean.csv
```

The raw dataset is not overwritten.

This allows the cleaning process to remain reproducible.

---

# 7. Exploratory Data Analysis

The EDA stage examines:

* Dataset dimensions.
* Column names.
* Data types.
* Missing values.
* Duplicate rows.
* Unique values.
* Numerical variables.
* Categorical variables.
* Descriptive statistics.
* Correlations.

---

# 8. Statistical Analysis

Numerical variables are analyzed using:

* Count.
* Mean.
* Median.
* Minimum.
* Maximum.
* Standard deviation.
* Variance.
* Quartiles.
* Interquartile range.
* Skewness.
* Kurtosis.

---

# 9. Visualization

The project generates:

* Correlation heatmaps.
* Box plots.
* Distribution plots.
* Histograms.
* Categorical count plots.

Generated figures are stored in:

```text
reports/figures/
```

---

# 10. Machine Learning

The main Machine Learning task is binary classification.

Target:

```text
Academic_Failure_Risk
```

Target values:

```text
0 = No Academic Failure Risk
1 = Academic Failure Risk
```

Potential algorithms include:

* Logistic Regression.
* Decision Tree.
* Random Forest.

---

# 11. Model Evaluation

Models will be evaluated using:

* Accuracy.
* Precision.
* Recall.
* F1-score.
* Confusion Matrix.
* ROC-AUC.

Models will be compared to determine which performs best for the dataset.

---

# 12. Research Questions

The project investigates questions such as:

### Digital Behavior

* Is social media usage associated with academic performance?
* Is AI tool usage associated with academic performance?

### Health

* Is sleep associated with burnout?
* Is physical activity associated with mental health?
* Is mental health associated with academic performance?

### Social Factors

* Is social isolation associated with burnout?
* Is social isolation associated with academic performance?

### Burnout

* Is burnout associated with academic performance?
* Can burnout help predict academic failure?

### Machine Learning

* Which variables are the strongest predictors of academic failure?
* Which classification algorithm performs best?
* How accurately can academic failure risk be predicted?

---

# 13. Reproducibility

The project aims to keep the analysis reproducible by:

* Keeping raw data separate from processed data.
* Using Python scripts for data processing.
* Saving generated visualizations.
* Defining dependencies in `requirements.txt`.
* Keeping data cleaning steps explicit.
* Avoiding modification of the original dataset.

---

# 14. Important Analytical Considerations

Correlation does not necessarily imply causation.

For example, finding a correlation between social media usage and academic performance does not prove that social media usage directly causes changes in academic performance.

Machine Learning results should also be interpreted carefully and should not be treated as evidence of causal relationships.

---

# 15. Current Development Stage

Current progress:

```text
Project Setup
      |
      v
Data Loading
      |
      v
Exploratory Data Analysis
      |
      v
Data Visualization
      |
      v
Correlation Analysis
      |
      v
Data Cleaning
      |
      v
CURRENT STAGE
      |
      v
Data Preprocessing
      |
      v
Feature Engineering
      |
      v
Machine Learning
      |
      v
Model Evaluation
```

The project is currently transitioning from exploratory analysis and visualization into structured data cleaning and preprocessing.
