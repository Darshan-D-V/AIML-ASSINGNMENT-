import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\Darshan D V\\Desktop\\Darshan D V AI With Cloud Computing SuprMentr Internship\\Assignment-10 Data Doctor (26-02-2026)\\dirty_data.csv.txt")

print("\n--- Original Data ---")
print(df)

# -------- Handle Missing Values --------
# Fill missing Age with mean
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Marks with 0
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

#Fill categorical columns with most frequent value
df["City"] = df["City"].fillna(df["City"].mode()[0])

# -------- Remove Duplicates --------
df.drop_duplicates()

# -------- Standardize Text --------
df["Name"] = df["Name"].str.strip().str.title()   # remove spaces + capitalize
df["City"] = df["City"].str.strip().str.title()   

#--------- Additional Cleaning---------
#Convert datatypes (if needed)
df["Age"] = df["Age"].astype(int)

# -------- Final Cleaned Data --------
print("\n--- Cleaned Data ---")
print(df)

#-------- Summary ---------
print("\n--- Summary ---")
print(df.describe())