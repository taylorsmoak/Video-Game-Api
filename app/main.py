from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import games

Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "Games",
        "description": "The games endpoint provides information on video games.",
    },
]

app = FastAPI(title='Video Game API', openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(games.router)


@app.get('/')
async def root():
    return {'message': 'test'}
