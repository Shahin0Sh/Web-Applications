from fastapi import FastAPI
import uvicorn
from routers.system import system_router
from services.system_service import check_data_exists, insert_kc_prices

app = FastAPI(debug=True)
app.include_router(system_router)

if not check_data_exists():
    insert_kc_prices()

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)