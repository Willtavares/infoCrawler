import bs4
import requests
from bs4 import BeautifulSoup

URL = 'https://revistaautoesporte.globo.com/rss/ultimas/feed.xml'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36 OPR/62.0.3331.116"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

titles = soup.findAll('title')
descriptions = soup.findAll('description')
# title = len(titles)
# description = len(descriptions)

for i in titles:
    print(i.text)
    for j in descriptions:
        print(j.text)

# print(descriptions)

# print(soup.prettify())

# print(title)



# import bs4
# from urllib.request import urlopen
# from bs4 import BeautifulSoup as soup

# url = urlopen("http://revistaautoesporte.globo.com/rss/ultimas/feed.xml")
# page = url.read()
# url.close()


# page_soup = soup(page, "html.parser")

# content = page.findAll("div", {"class":"collapsible"})

# print(content)
