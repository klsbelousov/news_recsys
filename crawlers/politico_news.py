from random import randint

import psycopg2
import requests
import lxml
from bs4 import BeautifulSoup
from config import host, user, password, database

#default_url = 'https://lenta.ru/parts/news'
url = 'https://lenta.ru'
category = 'politico'


try:

    connection = psycopg2.connect(
        host=host,
        user=user,
        database=database,
        password=password,
    )

    response = requests.get(url=url)
    main_page = BeautifulSoup(response.text, 'lxml')
    news_blocks = main_page.find_all('div', class_='topnews__column')
    for block in news_blocks:
        container = block.find_all('a', class_='card-mini _topnews')

        for pallete in container:
            link =  url + pallete.get('href')
            title = pallete.find('h3').text
            timestamp = pallete.find('time').text
            #print(time + '\n' +  title + '\n' + link + '\n')

            response = requests.get(url=link)
            page = BeautifulSoup(response.text, 'lxml')
            text = page.find('div', class_='topic-body__content').text

            #print(timestamp + '\n' + category + '\n' + title + '\n' + link + '\n' + text + '\n\n')

            with connection.cursor() as cursor:
                cursor.execute(
                    f'INSERT INTO news (timestamp, category, title, link, text) VALUES (%s, %s, %s, %s, %s);',
                    (timestamp, category, title, link, text)
                )
                connection.commit()
                print('[INFO] Data was successfully added')
        
        
except Exception as error:
    pass