from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, database
from sqlalchemy.orm import Session
from sqlalchemy import cast, Float

router = APIRouter(prefix='/ratings', tags=['Ratings'])


@router.get('/{rating}', response_model=list[schemas.VideoGame])
async def get_games_by_rating(rating: int, db: Session = Depends(database.get_db)):
    games = db.query(models.VideoGame).order_by(models.VideoGame.rating.desc()).filter(
        cast(models.VideoGame.rating, Float) >= rating, cast(models.VideoGame.rating, Float) < (rating + 1)).all()
    if not games:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No games with rating: {rating} were found')
    return games
