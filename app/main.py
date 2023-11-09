from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import titles, ids, release_dates, ratings, genres

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(titles.router)
app.include_router(ids.router)
app.include_router(release_dates.router)
app.include_router(ratings.router)
app.include_router(genres.router)


@app.get('/')
async def root():
    return {'message': 'test'}
