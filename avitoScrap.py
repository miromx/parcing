import requests
from bs4 import BeautifulSoup
import csv

search_word = 'ps4'
url = 'https://www.avito.ru/ramenskoe/igry_pristavki_i_programmy?q={}&p=1'.format(search_word)  # сегодня
page = requests.get(url)
soup = BeautifulSoup(page.content.decode('utf-8', 'ignore'), 'html.parser')

t = []
titles = soup.find_all('a', class_='snippet-link')
for title in titles:
    t.append(title.get_text('title', strip=True))
print(t)

p = []
prices = soup.find_all('span', class_='snippet-price')
for price in prices:
    p.append(price.get_text(strip=True))
# print(p)

l = []
links = soup.find_all('a', class_='snippet-link')
for link in links:
    link = 'https://www.avito.ru' + link.get('href')
    l.append(link)

d = zip(t, p, l)
result_list = list(d)

with open('{}.csv'.format(search_word), 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(zip(t, p, l))

# with open('test4pandas.csv', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter='\t')
#     writer.writerows(zip(t, p))

# with open('test4pandas.txt', 'w', encoding='utf-8', newline=None) as f:
#     for x, y in zip(t, p):
#         f.write('{}\t{}'.format(x, y))

# for x, y in zip(t, p):
#     # print('{}{}'.format(x, y))
#     print(x, y, '\n')
