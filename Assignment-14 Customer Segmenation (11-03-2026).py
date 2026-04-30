import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("C:\\Users\\Darshan D V\\Desktop\\Darshan D V AI With Cloud Computing SuprMentr Internship\\Assignment-14 Customer Segmenation (11-03-2026)\\mall_customers.csv")

# Select features
X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

# Apply K-Means
kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(X)

# Plot clusters
plt.figure()
plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()