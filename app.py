from fastapi import FastAPI
from routes.user import user

#Primero instanciamos FastAPI y damos nombre y descripcíon al proyecto
app=FastAPI(title='F1', description='carreras de formula 1')

app.include_router(user)

