from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix='/ratings', tags=['Ratings'])


# TODO: Figure out why there is an error when rating = 9, which makes the upper limit of filter 9 + 1 = 10
@router.get('/{rating}', response_model=list[schemas.VideoGame])
async def get_games_by_rating(rating: int, db: Session = Depends(database.get_db)):
    games = db.query(models.VideoGame).order_by(models.VideoGame.rating.desc()).filter(
        models.VideoGame.rating >= str(rating), models.VideoGame.rating < str(rating + 1)).all()
    if not games:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No games with rating: {rating} were found')
    return games
