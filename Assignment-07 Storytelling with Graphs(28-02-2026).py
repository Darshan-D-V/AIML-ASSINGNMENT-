import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\\Users\\Darshan D V\\Desktop\\Darshan D V AI With Cloud Computing SuprMentr Internship\\Assignment-06 Dataset Detective (24-02-2026)\\students.csv.txt")

# -------- BAR CHART --------
plt.figure()
df.groupby("City")["Marks"].mean().plot(kind="bar")
plt.title("Average Marks by City")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.show()

# -------- PIE CHART --------
plt.figure()
df["City"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Student Distribution by City")
plt.ylabel("")
plt.show()

# -------- HISTOGRAM --------
plt.figure()
df["Marks"].dropna().plot(kind="hist", bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()