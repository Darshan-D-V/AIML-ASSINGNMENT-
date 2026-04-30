import nltk
from nltk.corpus import wordnet as wn

# Download WordNet data (run once)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Function to compute similarity
def word_similarity(w1, w2):
    synsets1 = wn.synsets(w1)
    synsets2 = wn.synsets(w2)

    max_score = 0

    for s1 in synsets1:
        for s2 in synsets2:
            score = wn.path_similarity(s1, s2)
            if score and score > max_score:
                max_score = score

    return max_score

# Word pairs
pairs = [
    ("big", "large"),
    ("happy", "joyful"),
    ("car", "vehicle"),
    ("teacher", "educator"),
    ("hot", "warm")
]

# Calculate similarity
for w1, w2 in pairs:
    score = word_similarity(w1, w2)
    print(f"{w1} - {w2} : {score}")