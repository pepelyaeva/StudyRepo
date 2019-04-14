# === Download all files ===
import downloadManager
import os
currentDir = os.getcwd() 
dwnDir = currentDir + '/Files/DownloderApp/'
# downloadManager.download_manager('http://samlib.ru/', dwnDir)

import codecs

# folder = []
# for i in os.walk(dwnDir):
#     folder.append(i)

# === Run all files ===
# for address, dirs, files in folder:
#     for file in files:
#         print(address+'/'+file)
#         f = codecs.open(address+'/'+file, 'r')

f = codecs.open(dwnDir + "\samlib.ru\index.html", 'r')

# === Get all body text ===
import getHtmlText
text = getHtmlText.text_from_html(f)
# print(text)
# input()


# === Tokenize body text ===
import tokinizeBodyText
wordsFiltered = tokinizeBodyText.tokinize_text(text)
# print(wordsFiltered)


# === Get initial form, count words ===
from rutermextract import TermExtractor
import pymorphy2
import re, collections

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

l = lambda x: x[1]
print( *sorted(arr.items(), key=l, reverse=True), '\n' )

input()