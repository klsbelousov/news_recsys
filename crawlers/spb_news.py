from random import randint
from config import host, user, password, database

import psycopg2
import requests
import lxml
from requests import Session
from bs4 import BeautifulSoup

cities = {'SpB': 'https://www.spb.kp.ru', 'Moscow': 'https://www.msk.kp.ru'}

def check_duplicate(title):
        cur = connection.cursor()
        cur.execute("SELECT link FROM news WHERE title = %s", (title,))
        #print(cur.fetchone() is not None)
        return cur.fetchone() is not None

for city, url in cities.items():
    try:
        connection = psycopg2.connect(
                host=host,
                user=user,
                database=database,
                password=password,
            )

        category = city
        response = requests.get(url=url)
        main_page = BeautifulSoup(response.text, 'lxml')

        news_blocks = main_page.find('div', class_='sc-k5zf9p-13 fsrrpT')
        blocks = news_blocks.find_all('div', class_='sc-k5zf9p-1 kRfBQJ')
        for block in blocks:
            timestamp = block.find('time').get('datetime')
            title = block.find('a', class_='sc-k5zf9p-3 dqylVG').text
            link = url + block.find('a', class_='sc-k5zf9p-3 dqylVG').get('href')
            #print(time + '\n' + title + '\n' + link + '\n\n')
            response = requests.get(url=link)
            page = BeautifulSoup(response.text, 'lxml')
            paragraphs = page.find_all('p', class_='sc-1wayp1z-16 dqbiXu')
            text = ''

            for article in paragraphs:
                text += article.text
            
            if not (check_duplicate(title=title)):
                with connection.cursor() as cursor:
                    cursor.execute(
                        f'INSERT INTO news (timestamp, category, title, link, text) VALUES (%s, %s, %s, %s, %s);',
                        (timestamp, category, title, link, text)
                    )
                    connection.commit()
                    print('[INFO] Data was successfully added')
            else:
                break
        

    except Exception as error:
        print(error)

    finally:
        if connection:
            connection.close()

