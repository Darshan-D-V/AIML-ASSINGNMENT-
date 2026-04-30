import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load dataset
df = pd.read_csv("C:\\Users\\Darshan D V\\Desktop\\Darshan D V AI With Cloud Computing SuprMentr Internship\\Assignment-13 KNN in Real Life(07-03-2026)\\movies_data.csv.txt")

# Features (ratings)
X = df[["Action", "Comedy", "Drama"]]

# Train KNN model
model = NearestNeighbors(n_neighbors=3, metric='euclidean')
model.fit(X.values)

# Choose a movie (example: Avengers)
movie_index = df[df["Movie"] == "Titanic"].index[0]

# Find similar movies
distances, indices = model.kneighbors([X.iloc[movie_index]])

print("Selected Movie:", df.iloc[movie_index]["Movie"])
print("\nRecommended Movies:")

for i in range(1, len(indices[0])):  # skip itself
    print(df.iloc[indices[0][i]]["Movie"])