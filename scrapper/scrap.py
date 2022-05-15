import requests as r
from bs4 import BeautifulSoup
from time import sleep

headers = r.utils.default_headers()


def gen_data():
    info = []
    for page in range(1, 8):
        sleep(0.3)

        url = f'https://scrapingclub.com/exercise/list_basic/?page={page}'

        response = r.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')  # html.parser

        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

        for i in data:
            name = i.find('h4', class_='card-title').text.replace('\n', '')
            price = i.find('h5').text.replace('\n', '')
            url_thing = 'https://scrapingclub.com' + i.find('a').get('href')
            card = (name, price, url_thing)
            info.append(card)
    return info
