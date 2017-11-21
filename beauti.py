from bs4 import BeautifulSoup 
import requests 
import lxml 
import urllib3


agents = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

def scrape(url):
	get_page_data = requests.get(url, headers=agents)
	return BeautifulSoup(get_page_data.text, 'lxml')

def get_link(url):
	link_lists = []

	soup = scrape(url)	
	# From techcrunch	
	if "techcrunch" in url:
		from_tech = soup.findAll("h2", { "class" : "post-title" })[:20]

		# Extracting links 
		for data in from_tech:
			for data in data.findAll("a", href=True):
				link = data["href"]	
				link_lists.append(link)
	else:
		print("Wrong Input")	

	return (link_lists)

def get_data(url):
	title_lists = []
	img_src = []
	desc_lists = []
	description = ''

	soup = scrape(url)

	content = soup.find("div", {"class", "article-entry"})
	video_content = soup.find('div', {'class': 'vdb_player'})

	if "techcrunch" in url:
		if video_content:
			content.decompose()
		else:	
			for data in soup.find('title'): 
				title = data.string.replace("\xa0", " ")
				title_lists.append(title)
			#getting article image links
			for data in content.findAll('img', {"class", ""}):
				get_link = data["src"]
				img_src.append(get_link)

		# getting article description
		for data in content.findAll('p'):
			get_desc = data.text
			for ch in ['\xa0','\u200a']:
				if ch in get_desc:
					get_desc = get_desc.replace(ch, " ")
					description = description+'\n'+get_desc
			
	else:
		print("not found")
	
	desc_lists.append(description)
	return (title_lists, img_src, desc_lists)
	
# Calling functions
def main():
	url = ['https://techcrunch.com/popular/']

	links = []
	for address in url:
		links = get_link(address)

	title_lists = []	
	img_lists = []
	desc_lists = []
	for link in links:
		title_lists, img_lists, desc_lists = get_data(link)

	print(links)
	print(title_lists)
	print(img_lists)
	print(desc_lists)

main()
