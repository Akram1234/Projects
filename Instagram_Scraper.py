import requests
import re
from bs4 import BeautifulSoup


url = input("Instagram Profile URL: ")
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
data = soup.find_all('meta', attrs={'property': 'og:description'})
text = data[0].get('content').split()
user = '%s %s %s' % (text[-3], text[-2], text[-1])
followers = text[0]
following = text[2]
posts = text[4]
data = str(soup.find('script', attrs={'type': 'application/ld+json'}).get_text)
email = re.findall(r'[\w\.-]+@[\w\.-]+', data)
print('User:', user)
print('Followers:', followers)
print('Following:', following)
print('Posts:', posts)
print('Email:', email)

