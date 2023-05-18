import requests # Allows us to downlaod
from bs4 import BeautifulSoup # Enables gather

res = requests.get('https://news.ycombinator.com/news') # think of this as the search bar
print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
votes = soup.select('.score')
# # for item in soup.find_all(class_='score'):
# # 	score_li = list(item.text)
# # 	print(item)
# for item in soup.select('.titleline'):
# 	print(item[0].get('a'))
# 	# linked = item.get('a')
# 	# print(linked)



def create_custom_hn(links, votes):
	hn = []
	for index, item in enumerate(links):
		title = links[index].text
		href = links[index].get('href', None)
		points = int(votes[index].text.replace('points', ''))
		print(points)
		hn.append({'title': title, 'link': href})
	return hn

create_custom_hn(links, votes)