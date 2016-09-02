import urllib
import requests
from bs4 import BeautifulSoup as bs

url = 'http://tieba.baidu.com/p/2166231880'
response = requests.get(url)
html = bs(response.text,'lxml')

n = 1
for item in html.find_all('img', class_='BDE_Image'):
	urllib.urlretrieve(item['src'],'%s.jpg'%n)
	n += 1