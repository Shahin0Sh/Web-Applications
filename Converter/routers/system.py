from fastapi import APIRouter, Response


system_router = APIRouter(prefix='/system')


@system_router.get('/kc_info')
def get_kc_info():
    pass