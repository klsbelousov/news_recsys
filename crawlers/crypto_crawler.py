import requests
import lxml
from bs4 import BeautifulSoup

url = 'https://ru.investing.com/news/'

response = requests.get(url=url)

main_page = BeautifulSoup(response.text, 'lxml')

news_containers = main_page.find_all('div', class_='textDiv')
print(news_containers)