import os
currentDir = os.getcwd()
dwnDir = currentDir + '/Files/DownloderApp/'

folder = []
for i in os.walk(dwnDir):
    folder.append(i)
print(folder)
for address, dirs, files in folder:
    for file in files:
        print(address+'/'+file)
input()