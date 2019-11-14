"""
Based on https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
Based on https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25
"""
from selenium import webdriver
import requests
import urllib.request
import time
import json 
# from parseSrt import parseSrt
from bs4 import BeautifulSoup
import youtube_dl



options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
# list of tuples of uri and the number of lecture videos
uri_list = [('african-american-studies/afam-162', 25), ('astronomy/astr-160', 24)]


all_classes = {}
curr_class = None 
for uri in uri_list:
	print("Parsing class:", uri)
	all_lectures = {}
	curr_lecture = None
	for lecture_num in range(1, uri[1] + 1):
		url = 'https://oyc.yale.edu/' + uri[0] + '/lecture-{0}'.format(lecture_num)
		driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options)
		driver.get(url)
		link = driver.find_element_by_link_text('html')
		time.sleep(2)
		link.click()

		time.sleep(2)
		page_source = driver.page_source

		soup = BeautifulSoup(page_source, "html.parser")
		item_list_div = soup.find("div", {"id": "cboxLoadedContent"})

		
		curr_topic = None
		segmented_text = {}
		for child in item_list_div.findChildren():
			if child.name == 'h1':
				curr_class = child.get_text()
			elif child.name == 'h2':
				curr_lecture = child.get_text()
			elif child.name == "h3":
				curr_topic = child.get_text()
			elif child.name == 'p':
				if curr_topic is not None:
					segmented_text[curr_topic] = segmented_text.get(curr_topic, '') + child.get_text()
		all_lectures[curr_lecture] = segmented_text
	all_classes[curr_class] = all_lectures 
json.dump(all_classes, open('data/text_data.json', 'w', encoding='utf8'), indent=4, ensure_ascii=False)

# def download_subs(url, lang="en"):
#     opts = {
#         "skip_download": True,
#         "writesubtitles": "%(name)s.vtt",
#         "subtitlelangs": lang
#     }

#     with youtube_dl.YoutubeDL(opts) as yt:
#         yt.download([url])

# download_subs(url)
# parser = parseSrt("./data/2.vtt")
