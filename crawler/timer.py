import schedule
from crypto_news import crypto_news
from politico_news import political_news
from spb_news import cities_news
from sports_news import sport_news


def main():
    crypto_news()
    political_news()
    cities_news()
    sport_news()

def pending():
    
    schedule.every().hour.do(main)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    pending()