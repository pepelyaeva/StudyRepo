# avito.ru, результаты поиска по запросу "котята"

from bs4 import BeautifulSoup
import requests
import json

d = {}
# title, section, address, time, link
cont = requests.get('https://www.avito.ru/perm?q=котята').content
soup = BeautifulSoup(cont)
for i,item in enumerate(soup.find_all('div', { "class" : "description" })):
	d['kotik' + str(i)] = {'title': item.h3.a.text.replace('\n',''), 'section': item.find('div', {'class':'data'}).p.text}
print(json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False))
input()