import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
df = pd.read_csv("C:\\Users\\Darshan D V\\Desktop\\Darshan D V AI With Cloud Computing SuprMentr Internship\\Assignment-12 Spam Classifier Thinking (10-03-2026)\\spam_data.csv.txt")

# Features (text) and Labels
X = df["Message"]
y = df["Label"]

# Convert text to numbers
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Test prediction
test_msg = ["Call me when you are free"]
test_vec = vectorizer.transform(test_msg)

prediction = model.predict(test_vec)
print("Prediction:", prediction[0])