from fastapi import FastAPI
from .database import Base, engine
from .routers import titles

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(titles.router)


@app.get('/')
async def root():
    return {'message': 'test'}
