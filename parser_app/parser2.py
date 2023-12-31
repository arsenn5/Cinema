import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urljoin

URL = 'https://rezka.ag/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}


@csrf_exempt
def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


@csrf_exempt
def get_data(html, limit=5):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    rezka_films = []

    for item in items[:limit]:
        title_name = item.find('div', class_="b-content__inline_item-link").get_text()
        title_url = URL + item.find('a').get('href')
        description = item.find('div', class_="b-post__description").get_text()
        cover_div = item.find('div', class_="b-content__inline_item-cover")
        image_url = urljoin(URL, cover_div.find('img').get('src')) if cover_div and cover_div.find('img') else None

        rezka_films.append({
            "title_name": title_name,
            "description": description,
            "title_url": title_url,
            "image": image_url
        })

    return rezka_films[:limit]


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        all_films = []
        for page in range(0, 1):
            html = get_html('https://rezka.ag/', params=page)
            all_films.extend(get_data(html.text))
            # print(all_films)
        return all_films
    else:
        raise Exception('Error in parsing...')

# parser()
