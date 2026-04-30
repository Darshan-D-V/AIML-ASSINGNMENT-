from sklearn.feature_extraction.text import TfidfVectorizer

# Documents
docs = [
    "Machine learning is amazing and powerful",
    "Deep learning makes machines intelligent",
    "AI and machine learning are the future",
    "Data science uses machine learning techniques",
    "Artificial intelligence and deep learning are trending"
]

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(docs)

# Get feature names
feature_names = vectorizer.get_feature_names_out()

# Convert to array
tfidf_matrix = X.toarray()

# Find top words for each document
for i, doc in enumerate(tfidf_matrix):
    print(f"\nDocument {i+1} Top Keywords:")
    
    # Get top 3 words
    top_indices = doc.argsort()[-3:][::-1]
    
    for index in top_indices:
        print(feature_names[index], ":", doc[index])