import requests as r
from bs4 import BeautifulSoup as bs

def kc_prices(url: str) -> dict:
    
    page = r.get(url)    
    soup = bs(page.text, 'html.parser')
    data = soup.find('div', class_='mini-game-product-list mt-50 mb-50 hidden-lg hidden-xl')
    resp_data = {}

    for el in data:
        name = ((el.find('h2', class_='name')).text)[4:]
        price = (el.find('div', class_='new')).text

        if 'Hediye' in name:
            temp = name.split()
            kc_total = int(temp[0]) + int(temp[2][1:])
            resp_data[f'{kc_total} KC'] = price
        else:
            resp_data[name] = price

    return resp_data