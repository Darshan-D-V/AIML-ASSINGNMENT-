import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

# Download required data
nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text):
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize words
    words = word_tokenize(text)
    
    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Count word frequency
    freq = Counter(words)
    
    # Get top 5 keywords
    keywords = freq.most_common(5)
    
    return keywords

# Example input
text = "Artificial Intelligence is transforming the world. AI helps in automation, data analysis, and decision making."

# Output
print("The Important Keywords are:")
print("Keywords:", extract_keywords(text))