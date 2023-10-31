from fastapi import FastAPI
from .database import Base, engine
from .routers import titles, ids, release_dates, ratings

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(titles.router)
app.include_router(ids.router)
app.include_router(release_dates.router)
app.include_router(ratings.router)


@app.get('/')
async def root():
    return {'message': 'test'}
