import psycopg2
import requests
import lxml
from bs4 import BeautifulSoup
from config import host, user, password, database


def sport_news():
    url = 'https://www.sports.ru/'
    categories = ['football', 'hockey', 'basketball', 'boxing', 'tennis']

    def check_duplicate(title):
            cur = connection.cursor()
            cur.execute("SELECT link FROM news WHERE title = %s", (title,))
            return cur.fetchone() is not None    

    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            database=database,
            password=password,
        )

        for category in categories:

            full_url = url + category

            response = requests.get(url=full_url)
            main_page = BeautifulSoup(response.text, 'lxml')
            news_block = main_page.find_all('li', class_='aside-news-list__item js-active')

            for block in news_block:
                try:
                    timestamp = block.find('time').get('datetime')
                    title = block.find('a', class_='analyticsTrackClick link link_size_small link_color_black').text
                    link = block.find('a').get('href')
                
                    page_response = requests.get(url=link)
                    page = BeautifulSoup(page_response.text, 'lxml')
                    topic = page.find('article', class_='news-item js-active')
                    text = topic.find('div', class_='news-item__content js-mediator-article').text

                    if not (check_duplicate(title=title)):
                        with connection.cursor() as cursor:
                            cursor.execute(
                                f'INSERT INTO news (timestamp, category, title, link, text) VALUES (%s, %s, %s, %s, %s);',
                                (timestamp, category, title, link, text)
                            )
                            connection.commit()
                            print('[INFO] Data was successfully added')
                except (AttributeError, ConnectionError, OSError) as error:
                    pass
        
    except Exception as error:
        print(error)

    finally:
        if connection:
            connection.close()
            print('Crawling stopped')