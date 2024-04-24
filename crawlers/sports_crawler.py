import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.sports.ru/'

response = requests.get(url=url)
#print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
data = soup.find('ul', class_='aside-news-list list-reset aside-news-block__list')
content = data.find_all('li' , class_='aside-news-list__item js-active')
for i in content:
    text = i.find('a', class_="analyticsTrackClick link link_size_small link_color_black").text
    try:
        fires = i.find('span', class_='link link_size_small link_color_blue comment-count__value').text
    except AttributeError:
        fires = 'None'
    url_text = i.find('a', class_='analyticsTrackClick link link_size_small link_color_black').get('href')
    print(text + '\n' + fires + '\n' + url_text + '\n')
