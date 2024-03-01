import requests as r
from bs4 import BeautifulSoup as bs

url_rates = 'https://www.xe.com/currencyconverter/convert/?Amount=10&From=TRY&To=BGN'
url_kc = 'https://www.oyunone.com/knightonline1'

def get_rates(url):
    
    page = r.get(url)
    soup = bs(page.text, 'html.parser')
    try_currency = soup.find('p', class_='result__BigRate-sc-1bsijpp-1 dPdXSB')
    bgn_currency = soup.find('div', class_='unit-rates___StyledDiv-sc-1dk593y-0 iGxfWX')

    bgn_rate = float((bgn_currency.text).split()[-2])
    try_rate = float((try_currency.text).split()[0])

    return {'1 BGN': try_rate,
            '1 TRY': bgn_rate}


def get_kc_prices(url):
    
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

def convert_try_to_bgn(try_num: float, url_rates: str) -> float:
    rates = get_rates(url_rates)
    bgn_curr = rates['1 TRY']
    return round(try_num / float(bgn_curr), 3)

def convert_bgn_to_try(bgn: float, url_rates: str) -> float:
    rates = get_rates(url_rates)
    try_curr = rates['1 TRY']
    return round(bgn * float(try_curr), 3)


def upd_kc_prices(url_rates, url_kc_prices):

    kc_prices = get_kc_prices(url_kc_prices)
    pass

