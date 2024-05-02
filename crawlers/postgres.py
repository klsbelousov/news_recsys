import psycopg2
from config import host, user, database, password
#from crawlers import timestamp, category, title, link, text

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        database=database,
        password=password,
    )
    
    # creating a new table
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE news(
                id serial PRIMARY KEY,
                timestamp varchar,
                category varchar,
                title text,
                link varchar,
                text text
            )"""
        )
        connection.commit()
        print('Table created')


    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """
    #         DROP TABLE economic_news
    #         """
    #     )
    #     connection.commit()
    #     print('Table was deleted')

#     with connection.cursor() as cursor:
#         cursor.execute(
#             f"""
#             INSERT INTO sport_news(timestamp, category, title, link, text)
#             VALUES ({timestamp}, {category}, {title}, {link}, {text})
#             """
#         )
#         print('[INFO] Data was successfully added')
except Exception as error:
    print(error)

finally:
    if connection:
        connection.close()
    
    


        # print("PostgreSQL connection closed")