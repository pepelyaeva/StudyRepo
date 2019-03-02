import subprocess
import os
import codecs
from bs4 import BeautifulSoup
 
class Downloder():
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
# x = Downloder()
# x.download_manager('http://samlib.ru/', dwnDir)

f = codecs.open(dwnDir + "\samlib.ru\index.html", 'r')


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

print(text_from_html(f))
input()
