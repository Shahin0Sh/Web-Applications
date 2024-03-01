import requests as r
from bs4 import BeautifulSoup as bs


def get_rates(url: str) -> dict:
    
    page = r.get(url)
    soup = bs(page.text, 'html.parser')
    try_currency = soup.find('p', class_='result__BigRate-sc-1bsijpp-1 dPdXSB')
    bgn_currency = soup.find('div', class_='unit-rates___StyledDiv-sc-1dk593y-0 iGxfWX')

    bgn_rate = round(float((bgn_currency.text).split()[-2]), 3)
    try_rate = round(float((try_currency.text).split()[0]), 3)

    return {'1 BGN': f'{try_rate} TRY',
            '1 TRY': f'{bgn_rate} BGN'}