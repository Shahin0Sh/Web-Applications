from fastapi import APIRouter, Response, HTTPException
from services import system_service as ss

system_router = APIRouter(prefix='/kc_info')

@system_router.get('/')
def get_kc_info():
    
    return ss.get_data()

@system_router.get('/{amount_kc}')
def get_amount_kc(amount_kc: int):
    
    data = ss.get_amount_kc(amount_kc)

    if data is None:
        raise HTTPException(status_code=404, detail='No such amount found.')
    return data

@system_router.post('/')
def upd_data():
    data = ss.upd_kc_prices()

    return Response(status_code=201, content='Data updated.')