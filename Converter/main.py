from fastapi import FastAPI
import uvicorn
from routers.system import rates_router

app = FastAPI(debug=True)
app.include_router(rates_router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)