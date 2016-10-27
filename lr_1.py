# avito.ru, результаты поиска по запросу "котята"

from bs4 import BeautifulSoup
import requests

cont = requests.get('https://www.avito.ru/perm?q=котята').content
soup = BeautifulSoup(cont)
descr = soup.find('div', { "class" : "description" })
print (descr)
input()