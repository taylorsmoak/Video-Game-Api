from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix='/ratings', tags=['Ratings'])


@router.get('/{rating}', response_model=list[schemas.VideoGame])
async def get_games_by_rating(rating: int, db: Session = Depends(database.get_db)):
    games = db.query(models.VideoGame).order_by(models.VideoGame.rating.desc()).filter(
        models.VideoGame.rating >= str(rating), models.VideoGame.rating < str(rating + 1)).all()
    return games
