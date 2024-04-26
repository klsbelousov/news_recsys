import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://www.sports.ru/'

response = requests.get(url=url)

main_page = BeautifulSoup(response.text, 'lxml')

# Collecting news
data = main_page.find('ul', class_='aside-news-list list-reset aside-news-block__list')
content = data.find_all('li' , class_='aside-news-list__item js-active')
for topic in content:
    try:
        fires = topic.find('span', class_='link link_size_small link_color_blue comment-count__value').text
    except AttributeError:
        fires = 'None'
    topic_link = topic.find('a', class_='analyticsTrackClick link link_size_small link_color_black').get('href')
    
    page_response = requests.get(url=topic_link)
    page = BeautifulSoup(page_response.text, 'lxml')
    page_content = page.find('div', class_='news-item__content js-mediator-article').text
    print(page_content + fires + '\n')