import pandas as pd

# Load dataset (example: CSV file)
df = pd.read_csv("C:\\Users\\Darshan D V\\Desktop\\Darshan D V AI With Cloud Computing SuprMentr Internship\\Assignment-06 Dataset Detective (24-02-2026)\\students.csv.txt")

# Display top rows
print("\n--- Top 5 Rows ---")
print(df.head())

# Find column with highest average value (numeric only)
highest_col = df.select_dtypes(include='number').mean().idxmax()
print("\nColumn with highest average value:", highest_col)

# Count missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Basic dataset info
print("\n--- Dataset Info ---")
print(df.info())