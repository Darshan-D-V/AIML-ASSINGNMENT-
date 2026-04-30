import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("C:\\Users\\Darshan D V\\Desktop\\Darshan D V AI With Cloud Computing SuprMentr Internship\\Assignment-08 ML Idea Generator (02-03-2026)\\placement_data.csv.txt")

# Features (input)
X = df[["CGPA", "AptitudeScore", "Internships", "Projects"]]

# Target (output)
y = df["Placed"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Prediction (example student)
prediction = model.predict([[8.0, 75, 2, 3]])

print("Placement Prediction:", prediction[0])