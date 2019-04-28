import nltk
import pymorphy2

def get_names(allWords, textID):
    personesList = []
    prob_thresh = 0.4

    morph = pymorphy2.MorphAnalyzer()

    for word, score in allWords.items():
        for p in morph.parse(word):
            if 'Name' in p.tag and p.score >= prob_thresh:
                if score > 1:
                    personesList.append({'name': p.normal_form, 'scope': score, 'textID': textID})

    return personesList