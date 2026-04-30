import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Sample messy sentences
sentences = [
    "hey brooo 😂😂 whats up???",
    "i canttt gooo tdy 😭",
    "omg!!! this is sooo cool 😎🔥",
    "plzz send me d notes asap",
    "gud mrng frnds ☀️"
]

# Slang dictionary
slang_dict = {
    "brooo": "bro",
    "tdy": "today",
    "plzz": "please",
    "gud": "good",
    "mrng": "morning",
    "frnds": "friends",
    "asap": "as soon as possible",
    "omg": "oh my god",
    "d": "the"
}

# Function to clean text
def preprocess(text):
    
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove emojis
    text = re.sub(r'[^\w\s]', '', text)
    
    # 3. Replace slang
    words = text.split()
    words = [slang_dict[word] if word in slang_dict else word for word in words]
    
    # 4. Remove repeated letters (soooo → so)
    words = [re.sub(r'(.)\1+', r'\1', word) for word in words]
    
    # 5. Tokenization
    tokens = word_tokenize(" ".join(words))
    
    # 6. Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    return tokens

# Apply preprocessing
for s in sentences:
    print("Original:", s)
    print("Processed:", preprocess(s))
    print("------------------------")