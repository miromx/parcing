import requests
from bs4 import BeautifulSoup 

word = 'коготь '
# word = 'Beam Heat Treatment'
url = 'https://www.multitran.com/m.exe?l1=2&l2=1&s='
page  = requests.get(url+word)
soup  = BeautifulSoup(page.content.decode('utf-8','ignore'), 'html.parser')

subj_list = soup.find_all('td', class_='subj')
subj_query_list = []
# все элементы td с данным классом subj
for item in subj_list:
	# атрибут title у тега а
	# item = item.a.get('title')
	item = item.get_text()
	subj_query_list.append(item)
	# print(item.a.get('title'))

for counter, value in enumerate(subj_query_list):
    print(counter, value)

trans_list = soup.find_all('td', class_='trans')
item_query_list = []
for item in trans_list:
	# item_query = item.find_all('a')
	item_query = item.get_text()
	item_query_list.append(item_query)
	# print(item_query)
# print(item_query_list)
for counter, value in enumerate(item_query_list):
    print(counter, value)

	# for item_a in item_query:
	# 		print(item.a)
    
# print(subj_list)