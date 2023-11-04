from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix='/genres', tags=['Genres'])


@router.get('/{genre}', response_model=list[schemas.VideoGame])
async def get_games_by_genre(genre: schemas.genres, db: Session = Depends(database.get_db)):
    games = db.query(models.VideoGame).order_by(models.VideoGame.name).filter(
        getattr(models.VideoGame, genre) == 'True')
    if not games:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No games with genre: {genre} were found')
    return games
