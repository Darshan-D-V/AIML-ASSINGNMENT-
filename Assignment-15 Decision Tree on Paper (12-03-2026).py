import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\\Users\\Darshan D V\\Desktop\\Darshan D V AI With Cloud Computing SuprMentr Internship\\Assignment-15 Decision Tree on Paper (12-03-2026)\\play_tennis.csv")

# Encode categorical data
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])

# Features & target
X = df.drop("Play", axis=1)
y = df["Play"]

# Train model
model = DecisionTreeClassifier()
model.fit(X.values, y)

# Predict example
prediction = model.predict([[2, 1, 0, 1]])  # sample encoded values
print("Prediction:", "Yes" if prediction[0] == 1 else "No")

# Visualize tree
plt.figure(figsize=(10,6))
tree.plot_tree(model, feature_names=X.columns, class_names=["No","Yes"], filled=True)
plt.show()