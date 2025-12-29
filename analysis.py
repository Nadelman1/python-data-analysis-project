# Python Data Analysis Project
# This file will contain data loading, cleaning, and analysis code.
import pandas as pd

def main():
    # Load dataset
    df = pd.read_csv("data/sample_data.csv")

    print("=== Preview (first 5 rows) ===")
    print(df.head())

    print("\n=== Shape ===")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    print("\n=== Missing Values ===")
    print(df.isnull().sum())

    print("\n=== Average Income by Target ===")
    avg_income = df.groupby("target")["income"].mean()
    print(avg_income)

if __name__ == "__main__":
    main()
