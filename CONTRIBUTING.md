# Contributing Guide

Thank you for your interest in contributing to the AI & Social Media Impact on Student Health & Academic Performance project.

This project is primarily an educational Data Science project, and contributions that improve code quality, analysis, documentation, visualization, or Machine Learning are welcome.

---

## Getting Started

### 1. Fork the Repository

Create your own fork of the repository on GitHub.

### 2. Clone Your Fork

```bash
git clone https://github.com/aymanaljamal/ai-social-media-student-analysis.git
```

### 3. Enter the Project

```bash
cd ai-social-media-student-analysis
```

### 4. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Branching Strategy

Create a new branch for each change.

Examples:

```bash
git switch -c feature/new-analysis
```

```bash
git switch -c fix/data-cleaning
```

```bash
git switch -c docs/update-readme
```

Recommended branch prefixes:

| Prefix      | Purpose            |
| ----------- | ------------------ |
| `feature/`  | New functionality  |
| `fix/`      | Bug fixes          |
| `docs/`     | Documentation      |
| `refactor/` | Code restructuring |
| `test/`     | Tests              |
| `chore/`    | Maintenance        |

---

## Code Style

Please keep Python code:

* Simple.
* Readable.
* Beginner-friendly.
* Properly commented.
* Organized into small functions.
* Easy to test and maintain.

Use descriptive variable and function names.

Example:

```python
def clean_column_names(df):
    ...
```

is preferred over:

```python
def clean(df):
    ...
```

---

## Data Rules

Do not modify the original raw dataset directly.

Raw data should remain inside:

```text
data/raw/
```

Processed datasets should be stored inside:

```text
data/processed/
```

This keeps the original dataset available for reproducibility.

---

## Commit Messages

Use clear commit messages.

Examples:

```text
feat: add data cleaning pipeline
```

```text
fix: correct processed dataset path
```

```text
docs: update project documentation
```

```text
refactor: separate data loading from cleaning
```

```text
test: add data cleaning tests
```

---

## Pull Requests

Before opening a Pull Request:

1. Make sure your code works.
2. Run the project tests.
3. Check that generated files are correct.
4. Review your changes.
5. Write a clear Pull Request description.

A Pull Request should explain:

* What was changed.
* Why it was changed.
* How it was tested.

---

## Reporting Problems

If you find a bug, please create a GitHub Issue and include:

* A clear description.
* Steps to reproduce the problem.
* Expected behavior.
* Actual behavior.
* Relevant error messages.

---

## Questions and Suggestions

For questions, improvements, or suggestions, open a GitHub Issue with enough context for the problem or idea to be understood.

Thank you for helping improve the project.
