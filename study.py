import requests, re 
import lxml 
import urllib3
from bs4 import BeautifulSoup 
agents = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def scrape(url):
	get_page_data = requests.get(url, headers=agents)
	return BeautifulSoup(get_page_data.text, 'lxml')

soup = scrape('https://techcrunch.com/')

data = soup.findAll('a')[:2]
for d in data:
	if 'href' in d.attrs:
		print(d.attrs['href'])

# # lambda expression
# data = soup.findAll(lambda tag: len(tag.attrs) == 2)[:2]
# print(data)
# regular expression
# images = soup.findAll('img',{'src':  re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
# for i in images:
# 	print(i["src"])