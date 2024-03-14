import requests as r
from bs4 import BeautifulSoup as bs
from data.database import insert_query, update_query, read_query
from data.models import ResponseKCmod
from fastapi import HTTPException
from common.validators import KC_INGAME_CASH

def get_rates() -> dict:
    
    url_rates = 'https://www.xe.com/currencyconverter/convert/?Amount=10&From=TRY&To=BGN'
    page = r.get(url_rates)
    soup = bs(page.text, 'html.parser')
    try_currency = soup.find('p', class_='result__BigRate-sc-1bsijpp-1 dPdXSB')
    bgn_currency = soup.find('div', class_='unit-rates___StyledDiv-sc-1dk593y-0 iGxfWX')

    bgn_rate = float((bgn_currency.text).split()[-2])
    try_rate = float((try_currency.text).split()[0])

    return {'1 BGN': try_rate,
            '1 TRY': bgn_rate}


def get_kc_prices() -> dict:
    
    url_kc = 'https://www.oyunone.com/knightonline1'
    page = r.get(url_kc)    
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

def convert_try_to_bgn(try_num: float) -> float:
    rates = get_rates()
    bgn_curr = rates['1 TRY']
    return round(try_num / float(bgn_curr), 3)

def convert_bgn_to_try(bgn: float) -> float:
    rates = get_rates()
    try_curr = rates['1 TRY']
    return round(bgn * float(try_curr), 3)

def update_db(amount: int, price_try: float, 
              price_bgn: float, ingame_cash: float) -> None:
    
    update_query('''UPDATE kc SET price_tr = ?, price_bgn = ?, ingame_cash_gb = ?
                       WHERE amount_kc = ?''',
                       (price_try, price_bgn, ingame_cash, amount))


def insert_db(amount: int, price_try: float, 
              price_bgn: float, ingame_cash: float) -> None | ValueError:
    
    ans = insert_query('''INSERT INTO kc(amount_kc, price_tr, price_bgn, ingame_cash_gb)
                    VALUES(?,?,?,?)''', (amount, price_try, price_bgn, ingame_cash))

    if not ans:
        raise ValueError('Could not insert into the database.')

def ingame_cash_libr(amount) -> int | float:
    try:
        return KC_INGAME_CASH[amount]
    except:
        return 0

def update_ingame_cash_libr(data: dict) -> None:
    
    for key, value in data:
        key = key[3:]
        update_query('''UPDATE kc SET ingame_cash_gb = ?
                     WHERE amount_kc = ?''',(value, key))

def upd_kc_prices() -> None | HTTPException: # updated db

    kc_prices = get_kc_prices()

    if not kc_prices:
        raise HTTPException(status_code=404, detail='Rates not found.')

    for key, value in kc_prices.items():
        amount = int(key[:-3])
        price_try = float(value[1:].replace(',', '.'))
        price_bgn = convert_try_to_bgn(price_try)
        ingame_cash = ingame_cash_libr(amount)
        update_db(amount, price_try, price_bgn, ingame_cash)

def insert_kc_prices() -> None | HTTPException: # this func inserts data in the db when starting the app for the first time

    kc_prices = get_kc_prices()

    if not kc_prices:
        raise HTTPException(status_code=404, detail='Rates not found.')

    for key, value in kc_prices.items():
        amount = int(key[:-3])
        price_try = float(value[1:].replace(',', '.'))
        price_bgn = convert_try_to_bgn(price_try)
        ingame_cash = ingame_cash_libr(amount)
        insert_db(amount, price_try, price_bgn, ingame_cash)

def get_data() -> list[ResponseKCmod]:

    data = read_query('''SELECT amount_kc, price_tr, price_bgn, ingame_cash_gb FROM kc''')
    return [ResponseKCmod.from_query_result(*row) for row in data]

def get_amount_kc(amount: int) -> ResponseKCmod | None:

    data = read_query('''SELECT amount_kc, price_tr, price_bgn, ingame_cash_gb FROM kc
                      WHERE amount_kc = ?''', (amount,))
    
    return next((ResponseKCmod.from_query_result(*row) for row in data), None)

def check_data_exists() -> bool:

   return True if (read_query('''SELECT 1 FROM kc''')) else False