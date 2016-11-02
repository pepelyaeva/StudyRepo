# avito.ru, результаты поиска по запросу "котята"

from bs4 import BeautifulSoup
import requests
import json

d = {}
# title, section, address, time, link, price
cont = requests.get('https://www.avito.ru/perm?q=котята').content
soup = BeautifulSoup(cont)
for i,item in enumerate(soup.find_all('div', { "class" : "description" })):
	title = item.h3.a.text.replace('\n','')
	data = item.find('div', {'class':'data'})
	time = data.find('div', {'class':'clearfix'}).find('div', {'class':'date c-2'}).text.replace('\n','')
	try:
		address = data.find_all('p')[1].text
	except Exception:
		address = 'none'
	d['kotik' + str(i)] = {'title': title, 'section': data.contents[1].text, 'address':  address,'time': time}


# нужно придумать что-то получше чем переделывать в массив
# d['kotik' + str(i)] = {'title': title, 'section': data.p[0].text, 'address':  data.p[1].text, 'time': data.div}
# d['kotik'] = {'title': title, 'section': data.contents[1].text, 'address':  data.contents[2].text, 'time': data.contents[3].div.div.text}
print(json.dumps(d, sort_keys=False, indent=4, ensure_ascii=False))
# print(d)
input()