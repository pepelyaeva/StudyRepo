# === Download all files ===
import downloadManager
import os
currentDir = os.getcwd() 
dwnDir = currentDir + '\Files\DownloderApp'
# downloadManager.download_manager('http://samlib.ru/', dwnDir)

import codecs

authorsList = []
textsList = []
personesList = []
wordsList = []
allWordsList = []

fwAuthors = open(currentDir + "\\authors.txt","w+")
fwTexts = open(currentDir + "\\texts.txt","w+")
fwPersons = open(currentDir + "\\persons.txt","w+")

# === Run all files ===
folders = []
lenRun = 20
for i in os.walk(dwnDir):
    folders.append(i)
flag = False
for address, dirs, files in folders:
    for file in files:
        if lenRun == 0:
            flag = True
            break
        currentAddress = address + '\\' + file
        currentUrl = currentAddress.replace(dwnDir, '')
        currentUrl = currentUrl.replace('\\', '', 1)
        print(currentUrl)
        f = codecs.open(address + '\\' + file, 'r')

        from bs4 import BeautifulSoup
        import re

        soup = BeautifulSoup(f, 'html.parser')

        import getHtmlText
        import tokinizeBodyText
        import countWrds

        def isTextPage(soup):
            return (soup.find('center') != None) and (soup.body.center.h2 != None) and (soup.body.dd != None)

        # === Get text name ===
        def getAuthorName(soup):
            authorNameTag = soup.body.div.h3
            [s.extract() for s in authorNameTag(['small', 'br'])]
            authorName = re.sub("^\s+|\n|\r|:|\s+$", "", authorNameTag.text)
            return authorName

        # === Get text name ===
        def getTextName(soup):
            return soup.body.center.h2.text

        # === Get all text words ===
        def getTextWrds(soup):
            allText = getHtmlText.text_from_html(soup.body.dd) 
            wordsFiltered = tokinizeBodyText.tokinize_text(allText)        
            return countWrds.count_wrds(wordsFiltered)

        if isTextPage(soup):
            lenRun -= 1
            authorName = getAuthorName(soup)
            authorDict = {'name': authorName}
            if authorDict not in authorsList:
                authorsList.append(authorDict)
            authorID = authorsList.index(authorDict)

            textName = getTextName(soup)
            textDict = {'url': currentUrl, 'name': textName, 'authorID': authorID}
            textsList.append(textDict)
            textID = textsList.index(textDict)

            allWords = getTextWrds(soup)
            
            # === Get names ===
            import getNames
            curPresList = getNames.get_names(allWords, textID)
            personesList = personesList + curPresList
            def isName(word):
                for pers in curPresList:
                    if word == pers['name']:
                        return True
                return False

            for word, score in allWords.items():
                if not isName(word):
                    wordsList.append({'word': word, 'score': score, 'textID': textID})
    if flag:
        break

import json
with open(currentDir + '\\authors.txt', 'w') as file:
     file.write(json.dumps(authorsList, indent=2, ensure_ascii=False))

with open(currentDir + '\\texts.txt', 'w') as file:
     file.write(json.dumps(textsList, indent=2, ensure_ascii=False))

with open(currentDir + '\\persons.txt', 'w') as file:
     file.write(json.dumps(personesList, indent=2, ensure_ascii=False))

with open(currentDir + '\\words.txt', 'w') as file:
     file.write(json.dumps(wordsList, indent=2, ensure_ascii=False))

fwAuthors.close()
fwTexts.close()
fwPersons.close()
print('complete')
input()
