# Use robots.txt to understand what each website allows and disallows

import requests # Allows us to downlaod
from bs4 import BeautifulSoup # Enables gather
import pprint

res = requests.get('https://news.ycombinator.com/news') # think of this as the search bar
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')


links = soup.select('.titleline > a')
links2 = soup2.select('.titleline > a')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


# # for item in soup.find_all(class_='score'):
# # 	score_li = list(item.text)
# # 	print(item)
# for item in soup.select('.titleline'):
# 	print(item[0].get('a'))
# 	# linked = item.get('a')
# 	# print(linked)


def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:k['votes'], reverse=True)


def create_custom_hn(links, subtext):
	hn = []
	for index, item in enumerate(links): # Use enumerate because 
		title = item.text
		href = item.get('href', None)
		vote = subtext[index].select('.score')
		if len(vote):
			points = int(vote[0].text.replace('points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))