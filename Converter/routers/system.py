from fastapi import APIRouter, Response
from services import system_service as ss

system_router = APIRouter(prefix='/kc_info')

@system_router.get('/')
def get_kc_info():
    
    return ss.get_data()

@system_router.post('/')
def upd_data():
    ss.insert_kc_prices()
    return Response(status_code=201, content='Data created.')