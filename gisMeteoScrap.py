import requests
from bs4 import BeautifulSoup 

# word = 'airfoil'
# word = 'Beam Heat Treatment'
url = 'https://www.gismeteo.ru/weather-ramenskoye-11439/' # сегодня
# page  = requests.get(url+word)
page  = requests.get(url)
soup  = BeautifulSoup(page.content.decode('utf-8','ignore'), 'html.parser')

# subj_list = soup.find_all('td', class_='subj')
# # все элементы td с данным классом subj
# # for item in subj_list:
# 	# атрибут title у тега а
# 	# print(item.a.get('title'))

# trans_list = soup.find_all('td', class_='trans')

# for item in trans_list:
# 	item_query = item.find_all('a')
# 	print(item_query)

# 	# for item_a in item_query:
# 	# 		print(item.a)
    
# # print(trans_list)

subj_list = soup.find_all('div', class_='tab  tooltip')
print(subj_list)