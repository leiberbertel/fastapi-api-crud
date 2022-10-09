# Fastapi
from fastapi import FastAPI

# Database
from src.database import User
from src.database import database as connection


app = FastAPI(title='Practice API',
            description='Estamos en un prueba',
            version='1')


# Events
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    
    connection.create_tables([User])

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

# Path
@app.get('/')
async def index():
    return 'Hola mundo!'

@app.get('/about')
async def about():
    return 'Estamos en el about del servicio web'