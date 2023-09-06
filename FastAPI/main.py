
# Documentacion oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products, users,basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
#app.include_router(jwt_auth_users.router)

#Recursos estaticos
app.mount("/static",StaticFiles(directory="static"), name="static")

# url local: http://127.0.0.1:8000

@app.get("/")
async def root():
    return "¡Hola FastAPI!"

# url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL + C

# Documentacion con Swagger: http://127.0.0.1.8000/docs
# Documentacion con Redocly: http://127.0.0.1.8000/redoc

