# import psycopg2
# import requests
# from bs4 import BeautifulSoup
# from config import host, user, password, database


# url = 'https://www.sports.ru/'



# try:
#     connection = psycopg2.connect(
#         host=host,
#         user=user,
#         database=database,
#         password=password,
#     )

#     def check_duplicate(link):
#         cur = connection.cursor()
#         cur.execute("SELECT link FROM news WHERE link = %s", (link,))
#         print(cur.fetchone() is not None)
#         return cur.fetchone() is not None
                  
                    

#     full_url = url

#     response = requests.get(url=full_url)
#     main_page = BeautifulSoup(response.text, 'lxml')
#     news_block = main_page.find_all('li', class_='aside-news-list__item js-active')

#     for block in news_block:
#         link = str(block.find('a').get('href'))
#         check_duplicate(link=link)
            
            

        

# except Exception as error:
#     print(error)

# finally:
#     if connection:
#         connection.close()


if False:
    print(3+3)