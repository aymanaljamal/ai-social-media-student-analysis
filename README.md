<div align="center">

<img src="./reports/figures/dataset-cover.png" alt="AI and Social Media Impact on Student Health and Academic Performance" width="900">

# AI & Social Media Impact on Student Health & Academic Performance

### Data Analysis, Visualization, Data Cleaning, and Machine Learning Project

<p>

<a href="https://github.com/aymanaljamal/ai-social-media-student-analysis">
Repository
</a>

  |  

<a href="https://www.kaggle.com/datasets/debayank2024/ai-and-social-media-impact-student-health-and-grades">
Dataset
</a>

  |  

<a href="https://github.com/aymanaljamal/ai-social-media-student-analysis/tree/main/reports/figures">
Visualizations
</a>

</p>

</div>

---

# 📌 Project Overview

This project explores the relationship between **social media usage, AI tool usage, student health, burnout, social isolation, and academic performance**.

The project uses Python and common Data Science and Machine Learning libraries to build a complete and reproducible data analysis workflow.

The dataset contains:

* **15,000 student records**
* **14 original variables**

The dataset covers several areas related to student life and academic performance:

* Demographic information
* Social media usage
* AI tool usage
* Sleep
* Physical activity
* Mental health
* Physical health
* Social isolation
* Burnout
* Academic performance
* Academic failure risk

The project has progressed from initial data exploration and visualization to **data cleaning, preprocessing, feature engineering, Machine Learning, model evaluation, and report generation**.

---

# 🎯 Project Goals

The main goal is to understand how students' digital behavior, lifestyle, health, and academic characteristics are related.

The analysis focuses on:

* Daily social media usage
* Daily AI tool usage
* Sleep duration
* Physical activity
* Mental health
* Physical health
* Social isolation
* Burnout
* Academic performance
* Academic failure risk

The Machine Learning objective is to build a classification model capable of predicting:

```text
Academic_Failure_Risk
```

---

# 🔄 Project Workflow

The project follows a structured Data Science workflow:

```text
Raw Dataset
      |
      v
Data Loading
      |
      v
Data Exploration
      |
      v
Exploratory Data Analysis
      |
      v
Statistical Analysis
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
Data Preprocessing
      |
      v
Feature Engineering
      |
      v
Train/Test Split
      |
      v
Machine Learning
      |
      v
Model Evaluation
      |
      v
Report Generation
      |
      v
Model Saving
      |
      v
PDF Documentation
```

The project is designed using separate modules so that each stage can be maintained independently.

---

# 📊 Dataset

The project uses the public Kaggle dataset:

**AI & Social Media Impact: Student Health & Grades**

The original dataset is available on Kaggle:

[View Dataset on Kaggle](https://www.kaggle.com/datasets/debayank2024/ai-and-social-media-impact-student-health-and-grades)

The original raw dataset is stored locally in:

```text
data/raw/
```

The cleaned dataset is generated and stored in:

```text
data/processed/
```

The original raw dataset is never overwritten by the cleaning process.

## Dataset Statistics

| Property              |                   Value |
| --------------------- | ----------------------: |
| Records               |              **15,000** |
| Original Columns      |                  **14** |
| Numerical Variables   |                  **10** |
| Categorical Variables |                   **3** |
| Identifier            |                   **1** |
| Target Variable       | `Academic_Failure_Risk` |

---

# 📋 Dataset Columns

| Column                       | Type        | Description                |
| ---------------------------- | ----------- | -------------------------- |
| `Student_ID`                 | Identifier  | Unique student identifier  |
| `Age`                        | Numerical   | Student age                |
| `Gender`                     | Categorical | Student gender             |
| `Education_Level`            | Categorical | Student education level    |
| `Daily_Social_Media_Hours`   | Numerical   | Daily social media usage   |
| `Daily_AI_Tool_Usage_Hours`  | Numerical   | Daily AI tool usage        |
| `Sleep_Hours`                | Numerical   | Average daily sleep        |
| `Physical_Activity_Hours`    | Numerical   | Daily physical activity    |
| `Mental_Health_Score`        | Numerical   | Mental health score        |
| `Physical_Health_Score`      | Numerical   | Physical health score      |
| `Social_Isolation_Score`     | Numerical   | Social isolation score     |
| `Burnout_Level`              | Categorical | Student burnout level      |
| `Academic_Performance_Score` | Numerical   | Academic performance score |
| `Academic_Failure_Risk`      | Binary      | Academic failure risk      |

---

# 📁 Project Structure

```text
ai-social-media-student-analysis/
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   │
│   └── PULL_REQUEST_TEMPLATE.md
│
├── data/
│   ├── raw/
│   │   └── AI_SocialMedia_Student_Health_Dataset.csv
│   │
│   └── processed/
│       └── AI_SocialMedia_Student_Health_Dataset_clean.csv
│
├── models/
│   ├── random_forest_model.pkl
│   └── preprocessor.pkl
│
├── notebooks/
│   ├── 01_1_data_exploration.ipynb
│   ├── 01_2_data_exploration.ipynb
│   ├── 01_3_data_exploration.ipynb
│   ├── 02_analysis.ipynb
│   └── 03_machine_learning.ipynb
│
├── reports/
│   ├── figures/
│   │   ├── dataset-cover.png
│   │   ├── correlation_heatmap.png
│   │   ├── boxplot_*.png
│   │   ├── distribution_*.png
│   │   └── countplot_*.png
│   │
│   ├── models/
│   ├── metrics/
│   ├── matrices/
│   ├── tables/
│   │
│   └── notebooks/
│       ├── 01_1_data_exploration.pdf
│       ├── 01_2_data_exploration.pdf
│       ├── 01_3_data_exploration.pdf
│       ├── 02_analysis.pdf
│       └── 03_machine_learning.pdf
│
├── src/
│   ├── imports.py
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── data_analysis.py
│   ├── visualization.py
│   ├── preprocessing.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── tests/
│
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── PROJECT_DOCUMENTATION.md
├── README.md
├── SECURITY.md
├── requirements.txt
├── test.py
└── .gitignore
```

---

# 📓 Data Exploration Notebooks

The project contains notebooks documenting the exploratory data analysis process.

## `01_1_data_exploration.ipynb`

The first notebook focuses on understanding the dataset structure.

It includes:

* Loading the dataset
* Inspecting the dataset
* Checking dimensions
* Viewing column names
* Checking data types
* Viewing sample records
* Identifying numerical columns
* Identifying categorical columns

---

## `01_2_data_exploration.ipynb`

The second notebook focuses on statistical and categorical exploration.

It includes:

* Missing-value analysis
* Duplicate analysis
* Unique-value analysis
* Descriptive statistics
* Numerical variable analysis
* Categorical variable analysis
* Distribution inspection

---

## `01_3_data_exploration.ipynb`

The third notebook focuses on relationships between variables and visualization.

It includes:

* Correlation analysis
* Correlation heatmaps
* Numerical distributions
* Box plots
* Categorical count plots
* Visual exploration of important variables

---

## `02_analysis.ipynb`

The analysis notebook continues the project beyond the initial exploration stage.

It is used to organize the main analysis and prepare the project for Machine Learning.

The notebook includes:

* Cleaned dataset analysis
* Important variable relationships
* Target variable analysis
* Academic failure risk analysis
* Health-related relationships
* Digital behavior analysis
* Burnout analysis
* Machine Learning preparation
* Interpretation of important findings

---

## `03_machine_learning.ipynb`

The Machine Learning notebook documents the complete classification stage.

It includes:

* Loading the cleaned dataset
* Preparing features and target
* Feature engineering
* Train/test splitting
* Data preprocessing
* Feature encoding
* Feature scaling
* Random Forest training
* Model evaluation
* Confusion matrix
* Classification report
* Model saving
* Interpretation of results

---

# 📄 Project Reports & PDF Documentation

The project now includes **generated PDF reports** for the main Jupyter notebooks.

Each notebook was converted into a professional PDF report using the project's report utilities.

All generated PDF reports are stored in:

```text
reports/notebooks/
```

The reports provide a convenient way to review the project's analysis and Machine Learning results without opening Jupyter Notebook.

---

## 📘 01. Data Exploration Report

### `01_1_data_exploration.pdf`

This report documents the initial exploration of the dataset, including:

* Dataset structure
* Number of records
* Number of columns
* Column names
* Data types
* Sample records
* Numerical variables
* Categorical variables

[📄 Open 01_1 Data Exploration PDF](./reports/notebooks/01_1_data_exploration.pdf)

---

## 📗 02. Statistical Exploration Report

### `01_2_data_exploration.pdf`

This report contains the statistical exploration stage, including:

* Missing values
* Duplicate records
* Unique values
* Descriptive statistics
* Numerical analysis
* Categorical analysis
* Distribution analysis

[📄 Open 01_2 Data Exploration PDF](./reports/notebooks/01_2_data_exploration.pdf)

---

## 📙 03. Visualization & Correlation Report

### `01_3_data_exploration.pdf`

This report documents the visualization and correlation analysis stage.

It includes:

* Correlation heatmaps
* Box plots
* Distribution plots
* Histograms
* Count plots
* Relationship analysis

[📄 Open 01_3 Data Exploration PDF](./reports/notebooks/01_3_data_exploration.pdf)

---

## 📕 04. Main Analysis Report

### `02_analysis.pdf`

This report contains the main analytical stage of the project.

It focuses on:

* Cleaned data analysis
* Important relationships
* Academic performance
* Academic failure risk
* Digital behavior
* Health-related variables
* Burnout
* Social isolation
* Preparation for Machine Learning

[📄 Open 02 Analysis PDF](./reports/notebooks/02_analysis.pdf)

---

## 🤖 05. Machine Learning Report

### `03_machine_learning.pdf`

This report documents the Machine Learning pipeline.

It includes:

* Feature engineering
* Train/test split
* Preprocessing
* Random Forest model
* Model training
* Model evaluation
* Classification report
* Confusion matrix
* Model performance
* Saved model information

[📄 Open 03 Machine Learning PDF](./reports/notebooks/03_machine_learning.pdf)

---

# 🖼️ Report Preview

The PDF reports can also be represented using preview images stored inside:

```text
reports/figures/
```

For example:

```text
reports/figures/
├── report_01_1_preview.png
├── report_01_2_preview.png
├── report_01_3_preview.png
├── report_02_analysis_preview.png
└── report_03_machine_learning_preview.png
```

Once these preview images are added to the repository, they can be displayed directly in this README.

Example:

![Data Exploration Report](./reports/figures/report_01_1_preview.png)

[📄 Open Full PDF Report](./reports/notebooks/01_1_data_exploration.pdf)

---

# 🧹 Data Cleaning

A dedicated data-cleaning pipeline has been implemented in:

```text
src/data_cleaning.py
```

The data loading logic is separated into:

```text
src/data_loader.py
```

This modular structure makes the project easier to maintain and extend.

## Current Cleaning Steps

The cleaning pipeline performs:

1. Load the raw dataset.
2. Clean column names.
3. Clean text values.
4. Remove duplicate rows.
5. Convert numerical columns.
6. Handle missing values.
7. Validate numerical ranges.
8. Perform a final data check.
9. Save the cleaned dataset.

The cleaned dataset is saved to:

```text
data/processed/AI_SocialMedia_Student_Health_Dataset_clean.csv
```

The original raw dataset is not overwritten.

---

# 🔎 Exploratory Data Analysis

The project performs an initial inspection of the dataset before Machine Learning.

The analysis includes:

* Number of rows
* Number of columns
* Column names
* Data types
* Missing values
* Duplicate records
* Unique values
* Numerical columns
* Categorical columns
* Descriptive statistics
* Correlations

---

# 📈 Descriptive Statistics

For numerical variables, the project analyzes:

* Count
* Mean
* Median
* Minimum
* Maximum
* Standard deviation
* Variance
* Quartiles
* Interquartile range
* Skewness
* Kurtosis

---

# 📊 Data Visualization

Generated visualizations are stored in:

```text
reports/figures/
```

The project includes:

* Correlation heatmaps
* Box plots
* Numerical distribution plots
* Histograms
* Categorical count plots

---

# 🔥 Correlation Heatmap

The correlation heatmap is used to investigate relationships between numerical variables.

![Correlation Heatmap](./reports/figures/correlation_heatmap.png)

The analysis examines relationships involving variables such as:

* Social media usage
* AI tool usage
* Sleep
* Mental health
* Physical health
* Social isolation
* Academic performance

---

# 📦 Box Plots

Box plots are used to examine:

* Median
* Quartiles
* Data spread
* Potential outliers

### Age

![Age Box Plot](./reports/figures/boxplot_Age.png)

### Daily Social Media Usage

![Daily Social Media Usage](./reports/figures/boxplot_Daily_Social_Media_Hours.png)

### Daily AI Tool Usage

![Daily AI Tool Usage](./reports/figures/boxplot_Daily_AI_Tool_Usage_Hours.png)

### Sleep Hours

![Sleep Hours](./reports/figures/boxplot_Sleep_Hours.png)

### Physical Activity Hours

![Physical Activity Hours](./reports/figures/boxplot_Physical_Activity_Hours.png)

### Mental Health Score

![Mental Health Score](./reports/figures/boxplot_Mental_Health_Score.png)

### Physical Health Score

![Physical Health Score](./reports/figures/boxplot_Physical_Health_Score.png)

### Social Isolation Score

![Social Isolation Score](./reports/figures/boxplot_Social_Isolation_Score.png)

### Academic Performance Score

![Academic Performance Score](./reports/figures/boxplot_Academic_Performance_Score.png)

### Academic Failure Risk

![Academic Failure Risk](./reports/figures/boxplot_Academic_Failure_Risk.png)

---

# 📉 Numerical Distributions

Histograms and distribution plots are used to understand how numerical variables are distributed.

The analysis includes variables such as:

* Age
* Daily social media usage
* Daily AI tool usage
* Sleep
* Physical activity
* Mental health
* Physical health
* Social isolation
* Academic performance
* Academic failure risk

---

# 🧑‍🎓 Categorical Analysis

Categorical variables are analyzed using count plots.

## Gender

![Gender Distribution](./reports/figures/countplot_Gender.png)

## Education Level

![Education Level Distribution](./reports/figures/countplot_Education_Level.png)

## Burnout Level

![Burnout Level Distribution](./reports/figures/countplot_Burnout_Level.png)

`Student_ID` is treated as an identifier and should not be interpreted as a meaningful categorical feature.

---

# 🤖 Machine Learning

The project includes a complete Machine Learning pipeline for predicting:

```text
Academic_Failure_Risk
```

This is a binary classification problem:

```text
0 → No Academic Failure Risk
1 → Academic Failure Risk
```

The implemented Machine Learning workflow is:

```text
Cleaned Dataset
      |
      v
Feature Engineering
      |
      v
Train/Test Split
      |
      v
Preprocessing
      |
      v
Feature Encoding
      |
      v
Feature Scaling
      |
      v
Random Forest
      |
      v
Model Evaluation
      |
      v
Model Saving
```

---

# ⚙️ Machine Learning Preprocessing

The preprocessing pipeline is implemented in:

```text
src/preprocessing.py
```

The pipeline performs:

* Feature selection
* Feature engineering
* Train/test splitting
* Numerical preprocessing
* Categorical encoding
* Feature scaling
* Preprocessor fitting

## Feature Engineering

Three additional binary features are generated:

```text
Uses_AI_Tools
Is_Social_Media_User
Is_Physically_Active
```

These features represent simplified indicators of student behavior.

### `Uses_AI_Tools`

Indicates whether the student uses AI tools.

### `Is_Social_Media_User`

Indicates whether the student uses social media.

### `Is_Physically_Active`

Indicates whether the student participates in physical activity.

---

# ✂️ Train/Test Split

The dataset contains:

```text
Total records:   15,000

Training data:   12,000

Testing data:     3,000
```

An **80/20 train-test split** is used.

The preprocessing pipeline is fitted using the training data and then applied to the testing data.

This prevents information from the test dataset from being used during preprocessing.

---

# 🔢 Processed Features

After feature engineering, the Machine Learning dataset contains:

```text
16 features
```

## Numerical Features

```text
Age

Daily_Social_Media_Hours

Daily_AI_Tool_Usage_Hours

Sleep_Hours

Physical_Activity_Hours

Mental_Health_Score

Physical_Health_Score

Social_Isolation_Score

Academic_Performance_Score

Uses_AI_Tools

Is_Social_Media_User

Is_Physically_Active
```

## Categorical Features

```text
Student_ID

Gender

Education_Level

Burnout_Level
```

> `Student_ID` is an identifier rather than a meaningful behavioral feature. It should ideally be excluded from Machine Learning feature encoding in a future improvement to avoid unnecessarily increasing the feature space.

---

# 🧩 Preprocessing Pipeline

The preprocessing pipeline uses Scikit-learn components such as:

* `StandardScaler`
* `OneHotEncoder`
* `ColumnTransformer`

The numerical variables are scaled using:

```text
StandardScaler
```

Categorical variables are encoded using:

```text
OneHotEncoder
```

The preprocessing operations are combined using:

```text
ColumnTransformer
```

The preprocessor is fitted on the training data only.

---

# 🌲 Random Forest Model

The current implemented Machine Learning model is:

```text
Random Forest Classifier
```

Configuration:

```text
n_estimators = 100

random_state = 42

class_weight = balanced
```

The `class_weight="balanced"` option is used because the target classes are imbalanced.

---

# 🏋️ Model Training

The model training logic is implemented in:

```text
src/train_model.py
```

The training process:

1. Receives the prepared dataset.
2. Splits the data into training and testing sets.
3. Fits the preprocessing pipeline using training data.
4. Transforms the training and testing data.
5. Creates the Random Forest model.
6. Trains the model.
7. Saves the trained model.
8. Returns the model and test data required for evaluation.

---

# 📏 Model Evaluation

Model evaluation has been separated into a dedicated module:

```text
src/evaluate_model.py
```

The evaluation stage currently calculates:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report
* Confusion Matrix

Additional evaluation metrics such as ROC-AUC are planned for a future stage.

---

# 📊 Current Model Results

The Random Forest model was successfully trained and evaluated on the test dataset.

## Performance Summary

| Metric            |     Result |
| ----------------- | ---------: |
| Accuracy          | **98.47%** |
| Test Records      |  **3,000** |
| Class 0 Recall    |   **1.00** |
| Class 1 Recall    |   **0.77** |
| Class 1 Precision |   **0.97** |
| Class 1 F1-score  |   **0.86** |

---

# 📋 Classification Report

```text
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      2820
           1       0.97      0.77      0.86       180

    accuracy                           0.98      3000
   macro avg       0.98      0.88      0.92      3000
weighted avg       0.98      0.98      0.98      3000
```

The model achieved:

```text
Accuracy = 98.47%
```

---

# 🔲 Confusion Matrix

The current confusion matrix is:

```text
[[2816    4]
 [  42  138]]
```

The model correctly classified:

* **2,816** class-0 students
* **138** class-1 students

The model incorrectly classified:

* **4** class-0 students as class 1
* **42** class-1 students as class 0

The class-1 recall is:

```text
0.77
```

This means the model correctly identifies approximately **77% of the students who actually belong to the academic failure risk class**.

---

# ⚠️ Model Performance Interpretation

Although the model achieved a high accuracy of:

```text
98.47%
```

accuracy should not be considered the only important metric.

The target dataset is imbalanced:

```text
Class 0: 2,820 test records

Class 1:   180 test records
```

Therefore, metrics such as:

* Precision
* Recall
* F1-score
* Confusion Matrix
* ROC-AUC

are important for evaluating the model.

In particular, **class-1 recall** is important because class 1 represents students identified as being at academic failure risk.

The current model has:

```text
Class 1 Precision = 0.97
Class 1 Recall    = 0.77
Class 1 F1-score  = 0.86
```

This indicates that the model is highly precise when predicting the positive class, but it still misses some positive cases.

---

# 💾 Saved Machine Learning Files

After training, the following files are generated:

```text
models/

├── random_forest_model.pkl

└── preprocessor.pkl
```

## `random_forest_model.pkl`

Contains the trained Random Forest classification model.

## `preprocessor.pkl`

Contains the fitted preprocessing pipeline used to transform data before prediction.

These files can later be used to make predictions on new student records.

---

# ❓ Research Questions

## Digital Behavior

* Does higher social media usage relate to academic performance?
* Is AI tool usage associated with academic performance?
* How are social media and AI usage distributed among students?

## Health

* Is sleep duration related to burnout?
* Is physical activity associated with mental health?
* Is mental health related to academic performance?

## Social Factors

* Is social isolation associated with burnout?
* Is social isolation related to academic performance?

## Burnout

* How does burnout vary among students?
* Is burnout associated with academic performance?
* Can burnout help predict academic failure risk?

## Machine Learning

* Which variables are the strongest predictors of academic failure?
* Which classification model performs best?
* How accurately can academic failure risk be predicted?
* How can the recall of the academic failure risk class be improved?

---

# 🛠️ Technologies

## Python

Primary programming language used throughout the project.

## Pandas

Used for:

* Loading datasets
* DataFrame manipulation
* Data inspection
* Data cleaning
* Statistical analysis

## NumPy

Used for:

* Numerical operations
* Statistical calculations
* Numerical data processing

## Matplotlib

Used for creating and saving visualizations.

## Seaborn

Used for statistical visualizations such as:

* Heatmaps
* Box plots
* Histograms
* Count plots

## Scikit-learn

Used for the Machine Learning stage, including:

* Train/test splitting
* Encoding
* Feature scaling
* Preprocessing pipelines
* Random Forest classification
* Model evaluation

## Joblib

Used for saving trained Machine Learning models and preprocessing objects.

## Jupyter Notebook

Used for interactive and documented exploratory data analysis.

## Playwright

Used to convert generated Jupyter Notebook HTML files into PDF reports.

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/aymanaljamal/ai-social-media-student-analysis.git
```

Move into the project directory:

```bash
cd ai-social-media-student-analysis
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

For PDF report generation, install Playwright:

```bash
pip install playwright
```

Then install Chromium:

```bash
python -m playwright install chromium
```

---

# ▶️ Running the Project

## Run the Complete Machine Learning Pipeline

The main test script executes the Machine Learning workflow:

```bash
python test.py
```

The process includes:

```text
Load cleaned dataset
        |
        v
Feature engineering
        |
        v
Train/test split
        |
        v
Preprocessing
        |
        v
Random Forest training
        |
        v
Model saving
        |
        v
Model evaluation
        |
        v
Final results
```

---

# 🧹 Run Data Cleaning

The data-cleaning module can be executed using:

```bash
python src/data_cleaning.py
```

The cleaned dataset will be generated inside:

```text
data/processed/
```

---

# 📓 Run the Notebooks

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then navigate to:

```text
notebooks/
```

Available notebooks include:

```text
01_1_data_exploration.ipynb
01_2_data_exploration.ipynb
01_3_data_exploration.ipynb
02_analysis.ipynb
03_machine_learning.ipynb
```

---

# 📄 Generate PDF Reports

The project contains a report utility module responsible for organizing and generating project reports.

The report utilities are located in:

```text
utils/report_utils.py
```

The module can:

* Save figures
* Save Machine Learning models
* Save evaluation metrics
* Save confusion matrices
* Save classification reports
* Save DataFrames
* Save feature importance
* Save JSON reports
* Save text reports
* Convert Jupyter notebooks to PDF
* Convert all notebooks to PDF

The generated PDF reports are stored in:

```text
reports/notebooks/
```

The current generated reports are:

```text
reports/notebooks/

├── 01_1_data_exploration.pdf
├── 01_2_data_exploration.pdf
├── 01_3_data_exploration.pdf
├── 02_analysis.pdf
└── 03_machine_learning.pdf
```

The PDF conversion process uses:

```text
Jupyter Notebook
       |
       v
HTML
       |
       v
Playwright + Chromium
       |
       v
PDF Report
```

---

# 📚 Documentation

The project contains additional documentation:

| File                       | Purpose                                     |
| -------------------------- | ------------------------------------------- |
| `PROJECT_DOCUMENTATION.md` | Detailed technical project documentation    |
| `CHANGELOG.md`             | Project changes and development history     |
| `CONTRIBUTING.md`          | Contribution guidelines                     |
| `CODE_OF_CONDUCT.md`       | Community behavior guidelines               |
| `SECURITY.md`              | Security and vulnerability reporting policy |
| `LICENSE`                  | MIT open-source license                     |

---

# 🚧 Project Progress

## Project Setup

* [x] Create project structure
* [x] Create virtual environment
* [x] Create `.gitignore`
* [x] Create `requirements.txt`
* [x] Install required libraries

## Data Loading

* [x] Create `imports.py`
* [x] Create `data_loader.py`
* [x] Load CSV dataset
* [x] Verify dataset shape

## Data Exploration

* [x] Create `01_1_data_exploration.ipynb`
* [x] Create `01_2_data_exploration.ipynb`
* [x] Create `01_3_data_exploration.ipynb`
* [x] Inspect dataset dimensions
* [x] Inspect column names
* [x] Check data types
* [x] Identify numerical columns
* [x] Identify categorical columns
* [x] Check missing values
* [x] Check duplicate records
* [x] Analyze unique values
* [x] Calculate descriptive statistics
* [x] Calculate correlations
* [x] Analyze categorical variables

## Visualization

* [x] Create correlation heatmap
* [x] Create box plots
* [x] Create numerical distribution plots
* [x] Create categorical count plots
* [x] Save figures automatically
* [x] Store figures in `reports/figures/`
* [x] Exclude `Student_ID` from categorical visualization

## Data Cleaning

* [x] Create `data_cleaning.py`
* [x] Create `data_loader.py`
* [x] Clean column names
* [x] Clean text values
* [x] Remove duplicate rows
* [x] Convert numerical columns
* [x] Handle missing values
* [x] Validate numerical values
* [x] Create processed data directory
* [x] Save cleaned dataset

## Data Preprocessing

* [x] Prepare features and target
* [x] Train/test split
* [x] Encode categorical variables
* [x] Feature scaling
* [x] Feature engineering
* [x] Build preprocessing pipeline
* [x] Prevent preprocessing data leakage
* [ ] Outlier analysis
* [ ] Feature selection improvement
* [ ] Final feature optimization

## Machine Learning

* [x] Prepare features and target
* [x] Train/test split
* [x] Build Random Forest model
* [x] Train model
* [x] Save trained model
* [x] Save preprocessing pipeline

## Model Evaluation

* [x] Accuracy
* [x] Precision
* [x] Recall
* [x] F1-score
* [x] Classification report
* [x] Confusion matrix
* [ ] ROC-AUC
* [ ] ROC curve
* [ ] Precision-Recall curve

## Reports

* [x] Create report utilities
* [x] Create reports directory structure
* [x] Generate PDF report for `01_1_data_exploration.ipynb`
* [x] Generate PDF report for `01_2_data_exploration.ipynb`
* [x] Generate PDF report for `01_3_data_exploration.ipynb`
* [x] Generate PDF report for `02_analysis.ipynb`
* [x] Generate PDF report for `03_machine_learning.ipynb`
* [x] Store PDF reports inside `reports/notebooks/`
* [x] Add PDF reports to project documentation

## Model Comparison

* [ ] Logistic Regression
* [ ] Decision Tree
* [ ] Random Forest comparison
* [ ] Model comparison table
* [ ] Hyperparameter tuning
* [ ] Final best-model selection

## Advanced Analysis

* [ ] Analyze social media usage vs academic performance
* [ ] Analyze AI tool usage vs academic performance
* [ ] Analyze sleep vs burnout
* [ ] Analyze mental health vs burnout
* [ ] Analyze social isolation vs burnout
* [ ] Analyze burnout vs academic performance
* [ ] Identify important predictors of academic failure
* [ ] Feature importance visualization
* [ ] Build prediction interface

---

# 📌 Current Project Status

The project has successfully completed the main stages of the initial Data Science and Machine Learning pipeline.

```text
Project Setup
      |
      v
Data Loading
      |
      v
Data Exploration
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
Data Preprocessing
      |
      v
Feature Engineering
      |
      v
Train/Test Split
      |
      v
Machine Learning
      |
      v
Model Evaluation
      |
      v
PDF Report Generation
      |
      v
CURRENT STAGE
      |
      v
Model Improvement
      |
      v
ROC-AUC Analysis
      |
      v
Feature Importance
      |
      v
Model Comparison
      |
      v
Hyperparameter Tuning
      |
      v
Final Model Selection
```

The current Random Forest implementation achieved:

```text
Accuracy: 98.47%
```

on a test set containing:

```text
3,000 records
```

The positive-class performance was:

```text
Precision: 0.97
Recall:    0.77
F1-score:  0.86
```

The project has also generated **five PDF reports** documenting the major analysis and Machine Learning stages.

The next stage of the project is focused on:

* Model improvement
* Feature analysis
* ROC-AUC evaluation
* Feature importance
* Model comparison
* Hyperparameter tuning
* Final model selection

---

# 📖 Dataset Source

Original dataset:

**AI & Social Media Impact: Student Health & Grades**

Kaggle:

https://www.kaggle.com/datasets/debayank2024/ai-and-social-media-impact-student-health-and-grades

Project repository:

https://github.com/aymanaljamal/ai-social-media-student-analysis

Visualizations:

https://github.com/aymanaljamal/ai-social-media-student-analysis/tree/main/reports/figures

---

# 📑 PDF Reports

All generated PDF reports are available inside the repository:

| Report              | PDF                                                       |
| ------------------- | --------------------------------------------------------- |
| Data Exploration 01 | [Open PDF](./reports/notebooks/01_1_data_exploration.pdf) |
| Data Exploration 02 | [Open PDF](./reports/notebooks/01_2_data_exploration.pdf) |
| Data Exploration 03 | [Open PDF](./reports/notebooks/01_3_data_exploration.pdf) |
| Main Analysis       | [Open PDF](./reports/notebooks/02_analysis.pdf)           |
| Machine Learning    | [Open PDF](./reports/notebooks/03_machine_learning.pdf)   |

These reports are generated automatically from the Jupyter notebooks and are included in the GitHub repository for easy access and review.

---

# ⚠️ Important Note

This project is intended for educational and analytical purposes.

Correlation does not necessarily imply causation.

A statistical relationship between two variables should not automatically be interpreted as evidence that one variable directly causes the other.

The Machine Learning model is also an experimental educational model and should not be used as the sole basis for real-world academic or student-related decisions.

Although the current Random Forest model achieved **98.47% accuracy**, the target variable is imbalanced. Therefore, accuracy alone does not provide a complete picture of model performance.

Recall, precision, F1-score, confusion matrix, and future ROC-AUC analysis should also be considered.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# 👨‍💻 Author

**Ayman Al-Jamal**

GitHub:

https://github.com/aymanaljamal

Repository:

https://github.com/aymanaljamal/ai-social-media-student-analysis

---
