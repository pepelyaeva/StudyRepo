# avito.ru, результаты поиска по запросу "котята"

from bs4 import BeautifulSoup
import requests
import json

d = {}
home = 'https://www.avito.ru/perm'
cont = requests.get( home + '?q=котята' ).content
soup = BeautifulSoup(cont)
for i,item in enumerate(soup.find_all('div', { "class" : "description" })):
	title = item.h3.a.text.replace('\n','')
	link = item.h3.find('a').get('href')
	price = item.find('div', { "class" : "about" }).text.replace('\n','')
	price = [price, 'none'][price=='']
	data = item.find('div', {'class':'data'})
	time = data.find('div', {'class':'clearfix'}).find('div', {'class':'date c-2'}).text.replace('\n','')
	try:
		address = data.find_all('p')[1].text.replace('\n','')
	except Exception:
		address = 'none'
	d['kotik' + str(i)] = {'title': title, 'link': home+link, 'price': price, 'section': data.contents[1].text, 'address':  address,'time': time}
print(json.dumps(d, sort_keys=False, indent=4, ensure_ascii=False))
input()