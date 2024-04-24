import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.sports.ru/'

response = requests.get(url=url)

main_page = BeautifulSoup(response.text, 'lxml')

# Collecting top news
top_title = main_page.find('h1', class_='super-top__title').text
top_feature = main_page.find('p', class_='super-top__feature').text
top_link = main_page.find('a', class_='super-top__link link link_color_white analyticsTrackClick').get('href')
print(top_title + '\n' + top_feature + '\n' + top_link + '\n')

# Collecting news
data = main_page.find('ul', class_='aside-news-list list-reset aside-news-block__list')
content = data.find_all('li' , class_='aside-news-list__item js-active')
for topic in content:
    text = topic.find('a', class_="analyticsTrackClick link link_size_small link_color_black").text
    try:
        fires = topic.find('span', class_='link link_size_small link_color_blue comment-count__value').text
    except AttributeError:
        fires = 'None'
    topic_link = topic.find('a', class_='analyticsTrackClick link link_size_small link_color_black').get('href')
    print(text + '\n' + fires + '\n' + topic_link + '\n')
