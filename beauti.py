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
	i = 0
	title_lists = []
	link_lists = []

	soup = scrape(url)	
	# From techcrunch	
	if "techcrunch" in url:
		from_tech = soup.findAll("h2", { "class" : "post-title" })
		# Deleting the video news from data 

		# Extracting links 
		for title in from_tech:
			for data in title.findAll("a", href=True):
				title = data.string.replace("\xa0", " ")
				link = data["href"]	
				title_lists.append(title)
				link_lists.append(link)
				i = i + 1
			if i == 20:
				break		
	else:
		print("Wrong Input")	

	return (title_lists, link_lists)

def get_data(url):
	img_src = []
	desc_lists = []
	description = ''
	soup = scrape(url)

	content = soup.find("div", {"class", "article-entry"})
	video_content = soup.find('div', {'class': 'vdb_player'})

	if "techcrunch" in url:
		if video_content:
			soup.find("div", {"class", "article-entry"}).decompose()
		else:	
			#getting article image links
			for image in content.findAll('img', {"class", ""}):
				get_link = image["src"]
				img_src.append(get_link)

		# getting article description
		for desc in content.findAll('p'):
			get_desc = desc.text
			for ch in ['\xa0','\u200a']:
				if ch in get_desc:
					get_desc = get_desc.replace(ch, " ")
					description = description+'\n'+get_desc
			
	else:
		print("not found")
	
	desc_lists.append(description)
	return (img_src, desc_lists)
	
# Calling functions
def main():
	url = ['https://techcrunch.com/popular/']

	links = []
	title = []
	for address in url:
		title, links = get_link(address)

	img_lists = []
	description = []
	for link in links:
		img_lists, descrpition = get_data(link)

	print(links)
	print(title)
	print(img_lists)
	print(description)

main()
