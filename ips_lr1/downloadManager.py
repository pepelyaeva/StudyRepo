import subprocess
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