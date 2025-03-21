
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk

# Download necessary resources once
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')

# Sample text
sentence = "Rural-fintech Navadhan has raised Series A equity funding round with its initial target of 80 Cr oversubscribed to 111 Cr. The round is led by NabVentures, the venture Capital arm of NABARD"
# Tokenization
tokens = word_tokenize(sentence)
print("\nTokens:", tokens)

# POS tagging
pos_tags = pos_tag(tokens)  # Fixed overwriting issue
print("\nPOS Tags:", pos_tags)
