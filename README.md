

<div align="center">

<img src="./reports/figures/dataset-cover.png" alt="AI and Social Media Impact on Student Health and Grades" width="900">

# AI & Social Media Impact on Student Health & Academic Performance

### Data Analysis, Visualization, and Machine Learning Project

</div>
# AI & Social Media Impact on Student Health & Academic Performance

### Data Analysis, Visualization, and Machine Learning Project

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

# Project Overview

This project explores the relationship between social media usage, AI tool usage, student health, burnout, social isolation, and academic performance.

The dataset contains **15,000 student records** and **14 variables** covering demographic information, digital behavior, health indicators, burnout, academic performance, and academic failure risk.

The project follows a complete Data Science workflow:

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
Data Preprocessing
     |
     v
Machine Learning
```

---

# Project Goals

The main goals of this project are to investigate relationships between students' digital habits and their academic and health-related outcomes.

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

The final Machine Learning objective is to predict whether a student is at risk of academic failure.

---

# Dataset

The dataset used in this project is:

**AI & Social Media Impact: Student Health & Grades**

The original dataset is available on Kaggle:

[View Dataset on Kaggle](https://www.kaggle.com/datasets/debayank2024/ai-and-social-media-impact-student-health-and-grades)

The cleaned dataset used in this project is stored at:

```text
data/raw/AI_SocialMedia_Student_Health_Dataset_clean.csv
```

### Dataset Statistics

| Property              |                 Value |
| --------------------- | --------------------: |
| Records               |                15,000 |
| Columns               |                    14 |
| Numerical Variables   |                    10 |
| Categorical Variables |                     3 |
| Identifier            |                     1 |
| Target Variable       | Academic_Failure_Risk |

---

# Dataset Columns

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

# Project Structure

```text
ai-social-media-student-analysis/
│
├── data/
│   ├── raw/
│   │   └── AI_SocialMedia_Student_Health_Dataset_clean.csv
│   │
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── imports.py
│   ├── load_data.py
│   ├── data_analysis.py
│   └── visualization.py
│
├── reports/
│   └── figures/
│       ├── correlation_heatmap.png
│       ├── boxplot_*.png
│       ├── distribution_*.png
│       └── countplot_*.png
│
├── test.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Technologies

<div align="center">

<img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python" width="300"/>

</div>

## Python

Python is the primary programming language used throughout the project.

## Pandas

Used for:

* Loading the CSV dataset
* DataFrame manipulation
* Data inspection
* Statistical analysis
* Data processing

## NumPy

Used for:

* Numerical calculations
* Statistical operations
* Identifying numerical columns
* Data manipulation

## Matplotlib

Used for creating charts and saving visualizations.

## Seaborn

Used for statistical visualizations including:

* Correlation heatmaps
* Box plots
* Histograms
* Count plots

## Scikit-learn

Installed and prepared for the Machine Learning stage.

---

# Installation

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

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the test file:

```bash
python test.py
```

The program currently performs:

1. Dataset loading
2. Dataset inspection
3. Numerical column analysis
4. Categorical column analysis
5. Descriptive statistics
6. Correlation analysis
7. Data visualization
8. Saving generated figures

All generated visualizations are stored in:

```text
reports/figures/
```

---

# Exploratory Data Analysis

The project performs an initial inspection of the dataset before visualization and Machine Learning.

## Dataset Inspection

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

## Descriptive Statistics

For numerical variables, the project calculates:

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

# Data Visualization

The project generates multiple visualizations to make patterns and relationships easier to understand.

All figures are automatically saved to:

```text
reports/figures/
```

---

# Correlation Heatmap

The correlation heatmap shows the relationships between numerical variables.

![Correlation Heatmap](reports/figures/correlation_heatmap.png)

The heatmap helps identify positive and negative linear relationships between variables such as:

* Social media usage
* AI tool usage
* Sleep
* Mental health
* Physical health
* Social isolation
* Academic performance

---

# Box Plots

Box plots are used to examine:

* Median
* Quartiles
* Data spread
* Possible outliers

## Age

![Age Box Plot](reports/figures/boxplot_Age.png)

## Daily Social Media Usage

![Daily Social Media Usage](reports/figures/boxplot_Daily_Social_Media_Hours.png)

## Daily AI Tool Usage

![Daily AI Tool Usage](reports/figures/boxplot_Daily_AI_Tool_Usage_Hours.png)

## Sleep Hours

![Sleep Hours](reports/figures/boxplot_Sleep_Hours.png)

## Physical Activity Hours

![Physical Activity Hours](reports/figures/boxplot_Physical_Activity_Hours.png)

## Mental Health Score

![Mental Health Score](reports/figures/boxplot_Mental_Health_Score.png)

## Physical Health Score

![Physical Health Score](reports/figures/boxplot_Physical_Health_Score.png)

## Social Isolation Score

![Social Isolation Score](reports/figures/boxplot_Social_Isolation_Score.png)

## Academic Performance Score

![Academic Performance Score](reports/figures/boxplot_Academic_Performance_Score.png)

## Academic Failure Risk

![Academic Failure Risk](reports/figures/boxplot_Academic_Failure_Risk.png)

---

# Numerical Distributions

Histograms are used to understand how numerical variables are distributed across the dataset.

## Age

![Age Distribution](reports/figures/distribution_Age.png)

## Daily Social Media Usage

![Social Media Distribution](reports/figures/distribution_Daily_Social_Media_Hours.png)

## Daily AI Tool Usage

![AI Tool Usage Distribution](reports/figures/distribution_Daily_AI_Tool_Usage_Hours.png)

## Sleep Hours

![Sleep Distribution](reports/figures/distribution_Sleep_Hours.png)

## Physical Activity Hours

![Physical Activity Distribution](reports/figures/distribution_Physical_Activity_Hours.png)

## Mental Health Score

![Mental Health Distribution](reports/figures/distribution_Mental_Health_Score.png)

## Physical Health Score

![Physical Health Distribution](reports/figures/distribution_Physical_Health_Score.png)

## Social Isolation Score

![Social Isolation Distribution](reports/figures/distribution_Social_Isolation_Score.png)

## Academic Performance Score

![Academic Performance Distribution](reports/figures/distribution_Academic_Performance_Score.png)

## Academic Failure Risk

![Academic Failure Risk Distribution](reports/figures/distribution_Academic_Failure_Risk.png)

---

# Categorical Analysis

Count plots are used to understand the distribution of categorical variables.

## Gender

![Gender Distribution](reports/figures/countplot_Gender.png)

## Education Level

![Education Level Distribution](reports/figures/countplot_Education_Level.png)

## Burnout Level

![Burnout Level Distribution](reports/figures/countplot_Burnout_Level.png)

---

# Current Progress

## Project Setup

* [x] Create project structure
* [x] Create virtual environment
* [x] Create `.gitignore`
* [x] Create `requirements.txt`
* [x] Install required libraries

## Data Loading

* [x] Create `imports.py`
* [x] Create `load_data.py`
* [x] Load CSV dataset
* [x] Verify dataset shape
* [x] Display first rows

## Exploratory Data Analysis

* [x] Check dataset dimensions
* [x] Check column names
* [x] Check data types
* [x] Identify numerical columns
* [x] Identify categorical columns
* [x] Check missing values
* [x] Check duplicate records
* [x] Calculate count
* [x] Calculate mean
* [x] Calculate median
* [x] Calculate minimum
* [x] Calculate maximum
* [x] Calculate standard deviation
* [x] Calculate variance
* [x] Calculate quartiles
* [x] Calculate IQR
* [x] Calculate skewness
* [x] Calculate kurtosis
* [x] Analyze categorical variables
* [x] Calculate correlations

## Visualization

* [x] Create `visualization.py`
* [x] Correlation heatmap
* [x] Box plots
* [x] Numerical distribution plots
* [x] Categorical count plots
* [x] Save figures automatically
* [x] Store figures in `reports/figures/`
* [x] Exclude `Student_ID` from categorical visualization

## Data Preprocessing

* [ ] Handle missing values
* [ ] Check outliers
* [ ] Encode categorical variables
* [ ] Feature scaling
* [ ] Feature selection
* [ ] Feature engineering
* [ ] Create processed dataset

## Machine Learning

* [ ] Prepare features and target
* [ ] Train/test split
* [ ] Build baseline model
* [ ] Logistic Regression
* [ ] Decision Tree
* [ ] Random Forest
* [ ] Model evaluation
* [ ] Accuracy
* [ ] Precision
* [ ] Recall
* [ ] F1-score
* [ ] Confusion Matrix
* [ ] ROC-AUC
* [ ] Compare models
* [ ] Select best model
* [ ] Save trained model

## Advanced Analysis

* [ ] Analyze social media usage vs academic performance
* [ ] Analyze AI tool usage vs academic performance
* [ ] Analyze sleep vs burnout
* [ ] Analyze mental health vs burnout
* [ ] Analyze social isolation vs burnout
* [ ] Analyze burnout vs academic performance
* [ ] Identify important predictors of academic failure
* [ ] Build academic failure risk prediction model

---

# Machine Learning Objective

The primary Machine Learning objective is to predict:

```text
Academic_Failure_Risk
```

This is a binary classification problem:

```text
0 → No Academic Failure Risk

1 → Academic Failure Risk
```

Potential input features include:

```text
Age
Gender
Education_Level
Daily_Social_Media_Hours
Daily_AI_Tool_Usage_Hours
Sleep_Hours
Physical_Activity_Hours
Mental_Health_Score
Physical_Health_Score
Social_Isolation_Score
Burnout_Level
Academic_Performance_Score
```

Several classification algorithms will be tested and compared using standard evaluation metrics.

---

# Analysis Questions

The next stages of the project will investigate questions such as:

### Digital Behavior

* Does higher social media usage correlate with academic performance?
* Is AI tool usage associated with academic performance?
* How are social media and AI usage distributed among students?

### Health

* Is sleep duration related to burnout?
* Is physical activity associated with mental health?
* Is mental health related to academic performance?

### Social Factors

* Is social isolation associated with burnout?
* Does social isolation have a relationship with academic performance?

### Burnout

* How does burnout vary across students?
* Is burnout associated with academic performance?
* Can burnout help predict academic failure risk?

### Machine Learning

* Which variables are the strongest predictors of academic failure?
* Which classification algorithm performs best?
* Can academic failure risk be predicted accurately from student characteristics?

---

# Visualizations

All generated charts can be viewed in the repository:

[View all generated figures](https://github.com/aymanaljamal/ai-social-media-student-analysis/tree/main/reports/figures)

---

# Dataset Source

Original dataset:

**AI & Social Media Impact: Student Health & Grades**

Kaggle:

https://www.kaggle.com/datasets/debayank2024/ai-and-social-media-impact-student-health-and-grades

Project repository:

https://github.com/aymanaljamal/ai-social-media-student-analysis

---

# Important Note

This project is intended for educational and analytical purposes.

Correlation does not necessarily imply causation. Statistical relationships identified during the analysis should not automatically be interpreted as direct causal effects.

The Machine Learning models developed in later stages should also be evaluated carefully before making real-world decisions.

---

# Project Status

Current stage:

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
CURRENT STAGE COMPLETE
      |
      v
NEXT: Data Preprocessing
      |
      v
Machine Learning
```

The project has completed the initial Data Analysis and Visualization stage and is ready to move into Data Preprocessing and Machine Learning.

---

# Author

**Ayman Al-Jamal**

GitHub:

https://github.com/aymanaljamal

Repository:

https://github.com/aymanaljamal/ai-social-media-student-analysis
