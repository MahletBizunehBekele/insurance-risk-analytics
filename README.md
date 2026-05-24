# Insurance Risk Analytics

An end-to-end insurance risk analytics project focused on exploratory data analysis, portfolio risk evaluation, and reproducible machine learning workflows using GitHub Actions and DVC.

---

# Project Overview

This project analyzes an insurance portfolio dataset containing policy, customer, vehicle, premium, and claims information. The objective is to identify profitability patterns, regional risk differences, temporal claim trends, and high-risk customer segments through exploratory data analysis (EDA).

The project also demonstrates modern machine learning engineering practices including:

- Git-based version control
- Branch-based workflow development
- CI/CD automation using GitHub Actions
- Code quality validation with flake8
- Automated testing using pytest
- Data versioning and reproducibility using DVC

---

# Project Structure

```text
insurance-risk-analytics/
│
├── .github/workflows/      # CI/CD pipeline configuration
├── .dvc/                   # DVC configuration files
├── data/                   # Dataset directory (tracked via DVC)
├── notebooks/              # Jupyter notebooks
├── src/                    # Reusable Python utility modules
├── tests/                  # Pytest test files
├── models/                 # Placeholder for future ML models
├── pipelines/              # Placeholder for future ML pipelines
├── reports/                # Placeholder for reports/outputs
│
├── requirements.txt
├── .gitignore
├── .dvcignore
└── README.md
```

---

# Exploratory Data Analysis (Task 1)

The exploratory analysis focused on understanding portfolio profitability, claim behavior, and risk segmentation.

## Key Analyses Performed

### Data Quality Assessment
- Missing value analysis
- Data type inspection
- Numeric conversion and datetime preprocessing

### Business Metric Engineering
- Loss Ratio calculation
- Margin calculation

### Univariate Analysis
- Premium distributions
- Claims distributions
- Vehicle value distributions

### Outlier Detection
- Claims outlier analysis
- Vehicle value outlier analysis

### Geographic Analysis
- Province-level loss ratio comparison
- Province-level premium and claims trends
- Regional vehicle distribution analysis

### Temporal Analysis
- Monthly claims trends
- Monthly premium trends
- Trend fluctuation analysis

### Risk Segmentation
- Gender-based loss ratio analysis
- Vehicle type risk analysis
- Vehicle manufacturer risk analysis

### Correlation & Bivariate Analysis
- Correlation heatmap
- Premium vs claims relationship analysis

---

# CI/CD Pipeline

The project uses GitHub Actions for continuous integration and automated validation.

## Automated Checks
- Dependency installation
- flake8 code linting
- pytest test execution

## Workflow File

```text
.github/workflows/ci.yml
```

The CI pipeline automatically runs on:
- pushes to main
- pushes to task branches
- pull requests

---

# Data Version Control (Task 2)

This project uses DVC (Data Version Control) to manage large datasets and ensure reproducible workflows.

## Why DVC?

Git is inefficient for tracking large datasets and binary files. DVC solves this by:
- storing lightweight metadata in Git
- versioning datasets separately
- enabling reproducible ML workflows

---

# DVC Workflow

## Initialize DVC

```bash
dvc init
```

## Track Dataset

```bash
dvc add data/insurance_data.txt
```

This creates:
- `.dvc` metadata files
- automatic Git ignore rules for raw datasets

## Pull Dataset

```bash
dvc pull
```

## Push Dataset to Remote Storage

```bash
dvc push
```

---

# Reproducibility Workflow

This repository supports reproducible data workflows through:

- Git for source code tracking
- DVC for dataset versioning
- CI/CD validation pipelines
- Structured project organization

A collaborator can reproduce the project environment by:

```bash
git clone <repository-url>

pip install -r requirements.txt

dvc pull
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd insurance-risk-analytics
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Notebook

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/01_eda.ipynb
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Git
- GitHub Actions
- DVC
- Pytest
- flake8

---

# Key Insights

Some major findings from the analysis include:

- Significant regional differences in insurance loss ratios
- Strong skewness and outliers in claims distributions
- Variability in profitability across vehicle types and manufacturers
- Temporal fluctuations in claims activity
- Overall portfolio profitability with moderate average loss ratios

---

# Future Work

Future tasks may include:

- Feature engineering
- Predictive modeling
- Risk classification models
- Claim severity prediction
- Automated ML pipelines
- Experiment tracking
- Model deployment workflows

---

# Author

Mahlet Bizuneh Bekele