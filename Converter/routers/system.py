from fastapi import APIRouter, Response, HTTPException
from services import system_service as ss
from data.models import InGameCash

system_router = APIRouter(prefix='/kc_info')

@system_router.get('/', tags=['Get Kc info'])
def get_kc_info():
    
    return ss.get_data()

@system_router.get('/{amount_kc}', tags=['Get Kc info'])
def get_amount_kc(amount_kc: int):
    
    data = ss.get_amount_kc(amount_kc)

    if data is None:
        raise HTTPException(status_code=404, detail='No such amount found.')
    return data


@system_router.put('/', tags=['Update information'])
def upd_data():
    data = ss.upd_kc_prices()

    return Response(status_code=201, content='Data updated.')

@system_router.put('/ingame_price', tags=['Update information'])
def update_Ingame_kc_price(data: InGameCash):

    ss.update_ingame_cash_libr(data)

    return Response(status_code=201, content='Data updated.')
