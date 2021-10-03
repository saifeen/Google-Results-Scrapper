import requests
from bs4 import BeautifulSoup

query = input("Enter query: ").split("+")
url = "https://www.google.com/search?q={}".format(query)
info = requests.get(url).text
soup = BeautifulSoup(info,"html.parser")
heading = soup.find_all('h3')
link = soup.find_all('a',href=True)
li = list()
for l in link:
    if '/url' in l['href']:
        li.append((l['href'])[7:])
he = list()
for a in heading:
    he.append(a.get_text())

for i in range(len(he)):
    print(he[i] + "\n" + li[i] + "\n\n")