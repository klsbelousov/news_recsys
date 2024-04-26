import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://ru.investing.com/news/'
default_link = 'https://ru.investing.com'

response = requests.get(url=url)

main_page = BeautifulSoup(response.text, 'lxml')
news_containers = main_page.find_all('div', class_='textDiv')
for topic in news_containers:
    try:
        topic = topic.find('a')
        link = topic.get('href')
    except AttributeError:
        pass
    
    response = requests.get(url=default_link + link)
    page = BeautifulSoup(response.text, 'lxml')
    title = page.find('h1').text
    page_content = page.find('div', class_="article_WYSIWYG__O0uhw article_articlePage__UMz3q text-[18px] leading-8").text
    print(title + '\n' + page_content + '\n\n') 
    