# python-data-analysis-project
## Overview
This project demonstrates a simple end-to-end data analysis workflow using Python and pandas. The goal is to explore how income relates to a binary outcome using basic demographic and experience-related features.

## Dataset
The dataset is a small sample CSV containing:
- age
- income
- years of experience
- target (binary outcome: 0 or 1)

The data is stored in `data/sample_data.csv`.

## What This Project Does
- Loads a structured CSV dataset
- Inspects the data for shape and missing values
- Computes summary statistics
- Calculates average income grouped by the target variable

## Key Insight
In this dataset, individuals with a target value of 1 have a higher average income than those with a target value of 0. This demonstrates how simple grouping and aggregation can reveal relationships in structured data.

## Tools Used
- Python
- pandas
- GitHub Actions
