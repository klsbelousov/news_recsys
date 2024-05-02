import time
from random import randint
from config import host, user, password, database

import psycopg2
import requests
from requests import Session
import lxml
from bs4 import BeautifulSoup

url_default = 'https://cryptonews.net/ru/'
url = 'https://cryptonews.net'
category = 'crypto'

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        database=database,
        password=password,
    )
    response = requests.get(url=url_default)
    main_page = BeautifulSoup(response.text, 'lxml')
    news_blocks = main_page.find_all('div', class_="row news-item start-xs")
    for block in news_blocks:
        link = block.find('a', class_='title').get('href')

        response = requests.get(url=url+link)
        page = BeautifulSoup(response.text, 'lxml')

        title = page.find('h1').text
        text = page.find('div', class_='cn-content').text
    
        timestamp = block.find('div', class_="row middle-xs")
        timestamp = timestamp.find('span', class_='datetime flex middle-xs').text
        full_url = url+link


        with connection.cursor() as cursor:
                cursor.execute(
                    f'INSERT INTO news (timestamp, category, title, link, text) VALUES (%s, %s, %s, %s, %s);',
                    (timestamp, category, title, full_url, text)
                )
                connection.commit()
                print('[INFO] Data was successfully added')



except Exception as error:
    print(error)

finally:
    if connection:
        connection.close()




    

