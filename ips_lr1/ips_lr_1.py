﻿import wget
import time
import subprocess
import os
import codecs
 
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
x = Downloder()
x.download_manager('http://samlib.ru/', dwnDir)

f = codecs.open(dwnDir + "\index.html", 'r')
print(f.read())
input()
