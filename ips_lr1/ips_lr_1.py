import wget
import time
import subprocess

class Downloder():
    def download_manager(self, url, destination='Files/DownloderApp/', try_number="10", time_out="60"):
        #threading.Thread(target=self._wget_dl, args=(url, destination, try_number, time_out, log_file)).start()
		# if self._wget_dl(url, destination, try_number, time_out, log_file) == 0:
        if self._wget_dl(url, destination, try_number, time_out) == 0:
            return True
        else:
            return False


    def _wget_dl(self,url, destination, try_number, time_out):
        import subprocess
        command=["wget", "-c", "-P", destination, "-t", try_number, "-T", time_out , url]
        try:
            download_state=subprocess.call(command)
        except Exception as e:
            print(e)
        #if download_state==0 => successfull download
        return download_state

x = Downloder()
x.download_manager('http://samlib.ru/')