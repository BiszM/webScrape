import requests 
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
print(soup.get_text())	