from fastapi import FastAPI
import uvicorn
from routers.system import system_router

app = FastAPI(debug=True)
app.include_router(system_router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)