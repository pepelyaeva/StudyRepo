import re
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

def tokinize_text(text):
    tokenizer = RegexpTokenizer(r'\w+')

    stopWords = set(stopwords.words('russian'))
    words = tokenizer.tokenize(text)
    wordsFiltered = []
    for w in words:
        if w not in stopWords and len(w) > 2 and w.isalpha():
            wordsFiltered.append(w)
    return wordsFiltered