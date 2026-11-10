import requests
from bs4 import BeautifulSoup
import json
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
response = requests.get('https://www.kinopoisk.ru/series/1048575/')
soup = BeautifulSoup(response.text, 'html.parser')

class CodeError(Exception):
    print("Error: Invalid status code")
    logging.error("Error: Invalid status code")

if response.status_code == 200:
    # print(soup.prettify())
    title = soup.find('h1', class_='styles_title__h1__2xH4b').text.strip()
    year = soup.find('span', class_='styles_year__2BzvG').text.strip()
    rating = soup.find('span', class_='styles_ratingValue__1rj_J').text.strip()
    description = soup.find('div', class_='styles_description__3ZQzD').text.strip()

    data = {
        'title': title,
        'year': year,
        'rating': rating,
        'description': description
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        get_value = json.dump(data, f, ensure_ascii=False, indent=4)
else:
    logging.error(f'Error: {response.status_code}')
    CodeError()

