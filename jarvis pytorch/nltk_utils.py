import nltk
import numpy as np
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("english")

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    stemmed_words = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in stemmed_words:
            bag[idx] = 1.0
    return bag

email = stem('Wikipedia')
print(email)