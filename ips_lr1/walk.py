import os
currentDir = os.getcwd()
dwnDir = currentDir + '/Files/DownloderApp/'
fw = open(currentDir + "\\txt1.txt","w+")

folder = []
for i in os.walk(dwnDir):
    folder.append(i)

# for address, dirs, files in folder:
#     for file in files:
fw.write('сроврап вапруло')
fw.close()
print('complite')
input()