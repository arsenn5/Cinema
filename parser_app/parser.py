from bs4 import BeautifulSoup as bs
import requests
from django.views.decorators.csrf import csrf_exempt

URL = "http://www.manascinema.com/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

# start
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# get data
@csrf_exempt
def get_data(html):
    if html.status_code == 200:
        soup = bs(html.text, 'html.parser')
        items = soup.find_all('div', class_='short_movie_info')
        manas_film = []

        for item in items:
            manas_film.append({
                "title_name": item.find("div", class_='m_title').get_text(),
                "title_url": URL + item.find("a").get('href'),
                "image": URL + item.find('div', class_='m_thumb').find('img').get('src')
            })
        return manas_film
    else:
        raise Exception('Error in parsing...')

# endparser
@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        manas_films = []
        for page in range(0, 1):
            html = get_html(f'http://www.manascinema.com/movies', params=page)
            manas_films.extend(get_data(html))
            # print(manas_films)
        return manas_films

    else:
        raise Exception('Error in parsing...')

# parser()