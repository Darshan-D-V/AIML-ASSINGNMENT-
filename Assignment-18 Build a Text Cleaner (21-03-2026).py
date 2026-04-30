import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download once
nltk.download('punkt')
nltk.download('stopwords')

# Function to clean text
def clean_text(text):
    
    # 1. Convert to lowercase
    text = text.lower()
    
    # 2. Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # 3. Tokenize
    words = word_tokenize(text)
    
    # 4. Remove stopwords
    stop_words = set(stopwords.words('english'))
    cleaned_words = [word for word in words if word not in stop_words]
    
    # Join back to sentence
    return " ".join(cleaned_words)

# Test sentences
sentences = [
    "Hello!!! How are you doing today?",
    "This is a simple NLP example.",
    "I am learning Machine Learning and AI!"
]

# Apply cleaner
for s in sentences:
    print("Original:", s)
    print("Cleaned :", clean_text(s))
    print("----------------------")