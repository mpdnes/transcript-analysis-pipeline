import nltk
from nltk.text import Text

class Word:
    def __init__(self, word, bigrams, tf, idf, tf_idf, doc):
        self.word = word
        self.bigrams = bigrams
        self.pos = nltk.pos_tag(word)
        self.doc = doc
        self.tf = tf
        self.idf = idf
        self.tf_idf = tf_idf






