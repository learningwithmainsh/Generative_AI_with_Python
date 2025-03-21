# from NLTK Library - Stemming
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import nltk

# Download necessary NLTK data
nltk.download('punkt')

# Sample text 
text = "Running ran easily quickly."

# Tokenization of corpus
tokenize_words = word_tokenize(text)
print(f"\nTokenized Words: {tokenize_words}")

# Apply Stemming - Porter Stemmer
porter_stemmer = PorterStemmer()
porter_stemmed = [porter_stemmer.stem(word) for word in tokenize_words]
print(f"\nPorter Stemmed Words: {porter_stemmed}")

# Apply Stemming - Lancaster Stemmer
lancaster_stemmer = LancasterStemmer()
lancaster_stemmed = [lancaster_stemmer.stem(word) for word in tokenize_words]
print(f"\nLancaster Stemmed Words: {lancaster_stemmed}")
