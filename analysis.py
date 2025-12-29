# Python Data Analysis Project
# This file will contain data loading, cleaning, and analysis code.
import pandas as pd

def main():
    # Load dataset
    df = pd.read_csv("data/sample_data.csv")

    # Show a quick preview
    print("=== Preview (first 5 rows) ===")
    print(df.head(), end="\n\n")

    # Basic info
    print("=== Shape ===")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}", end="\n\n")

    print("=== Column Types ===")
    print(df.dtypes, end="\n\n")

    # If your dataset has a numeric column, this gives summary stats
    print("=== Summary Stats (numeric columns) ===")
    print(df.describe())

if __name__ == "__main__":
    main()
