from bs4 import BeautifulSoup 
import requests 
import lxml 
import urllib3, re


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
	title_content = soup.find('h1', {'class': 'tweet-title'})
	video_content = soup.find('div', {'class': 'vdb_player'})
	img_content = content.findAll('img', {"class", ""})
	desc_content = content.findAll('p')
	if "techcrunch" in url:
		if video_content or not(img_content) or not(desc_content) or not(title_content):
			content.decompose()	

		else:	
			for data in title_content: 
				title = data.string.replace("\xa0", " ")
				if title != '':
					title_lists.append(title)
			#getting article image links

			for data in img_content:
				get_link = data["src"]
				if img_content != '':
					img_src.append(get_link)

		# getting article description
		for data in desc_content:
			get_desc = data.text
			# get_new_desc = re.sub('[\xa0][\u200a]',' ', get_desc)
			get_new_desc = get_desc.replace('\xa0', ' ')
			if get_new_desc != '':
				description = description+'\n'+get_new_desc

			
	else:
		print("error url")
	
	desc_lists.append(description)
	if not title_lists or not desc_content or not img_src:
		return ('not', 'not', 'not')
	else:
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
		title, img, desc = get_data(link)
		if title == 'not' or img == 'not' or desc == 'not':
			print("not appended")
		else:
			title_lists.append(title)
			img_lists.append(img)
			desc_lists.append(desc)

	for t in title_lists:
		print(t)
	for t in img_lists:
		print(t)
	for t in desc_lists:
		print(t)	
	# print(desc_lists)

main()
