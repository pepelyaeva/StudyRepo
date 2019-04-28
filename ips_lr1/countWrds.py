from rutermextract import TermExtractor
import pymorphy2
import re, collections

def count_wrds(wordsFiltered):
    arr = collections.defaultdict(int)
    res_dict={}
    morph = pymorphy2.MorphAnalyzer()

    te=[]
    for a in wordsFiltered:
        try:
            te.append(morph.parse(str(a))[0].inflect({'sing', 'nomn'}).word)
        except Exception:
            continue

    for t1 in te: arr[t1] += 1

    return arr