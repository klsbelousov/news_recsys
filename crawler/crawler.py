import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.sports.ru/'

response = requests.get(url=url)
#print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
data = soup.find('ul', class_='aside-news-list list-reset aside-news-block__list')
content = data.find('li' , class_='aside-news-list__item js-active')
text = content.find('a', class_="analyticsTrackClick link link_size_small link_color_black").text
url_text = content.find('a', class_='analyticsTrackClick link link_size_small link_color_black').get('href')
print(text, url_text)
