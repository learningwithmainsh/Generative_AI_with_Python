import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download required NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a function for lemmatization
def lemmatize_words(text):
    words = nltk.word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)

# Sample text
text = "The cats are running and the children were playing"

# Perform lemmatization
lemmatized_text = lemmatize_words(text)
print("Original Text: ", text)
print("Lemmatized Text: ", lemmatized_text)
