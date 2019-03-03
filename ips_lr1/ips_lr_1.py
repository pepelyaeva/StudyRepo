import subprocess
import os
import codecs
from bs4 import BeautifulSoup
 

def download_manager(self, url, destination='Files/DownloderApp/', depth="1", try_number="10", time_out="60"):
    if self._wget_dl(url, destination, depth, try_number, time_out) == 0:
        return True
    else:
        return False


def _wget_dl(self,url, destination, depth, try_number, time_out):
    import subprocess
    command=["wget", "-r", "-l", depth, "-c", "-P", destination, "-t", try_number, "-T", time_out , "-nc", url]
    try:
        download_state=subprocess.call(command)
    except Exception as e:
        print(e)
    return download_state

currentDir = os.getcwd()
dwnDir = currentDir + '/Files/DownloderApp/'

# download_manager('http://samlib.ru/', dwnDir)

folder = []
for i in os.walk(dwnDir):
    folder.append(i)

# Run all files
for address, dirs, files in folder:
    for file in files:
        print(address+'/'+file)

    f = codecs.open(address+'/'+file, 'r')

    # Get all body text
    from bs4 import BeautifulSoup
    from bs4.element import Comment

    def tag_visible(element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def text_from_html(body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)
    text = text_from_html(f)

    # print(text)
    # input()
    ##########

    # Tokenize body text
    import re
    from nltk.corpus import stopwords
    from nltk.tokenize import RegexpTokenizer

    tokenizer = RegexpTokenizer(r'\w+')

    stopWords = set(stopwords.words('russian'))
    words = tokenizer.tokenize(text)
    wordsFiltered = []
    
    for w in words:
        if w not in stopWords and len(w) > 2 and w.isalpha():
            wordsFiltered.append(w)
    
    # print(wordsFiltered)

    #####

    # Get initial form, count words
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