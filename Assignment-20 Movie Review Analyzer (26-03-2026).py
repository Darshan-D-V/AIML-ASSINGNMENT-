import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dataset
data = {
    "Review": [
        "This movie is amazing and fantastic",
        "I really loved the acting",
        "Worst movie ever",
        "The plot was boring and slow",
        "Absolutely wonderful experience"
    ],
    "Sentiment": ["Positive", "Positive", "Negative", "Negative", "Positive"]
}

df = pd.DataFrame(data)

# Features & Labels
X = df["Review"]
y = df["Sentiment"]

# Convert text → numbers
vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

# Test on 5 reviews
test_reviews = [
    "I love this movie",
    "This was terrible",
    "Amazing story and acting",
    "Very boring film",
    "Best movie ever"
]

test_vec = vectorizer.transform(test_reviews)
predictions = model.predict(test_vec)

# Output
for review, pred in zip(test_reviews, predictions):
    print(review, "→", pred)