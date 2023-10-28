from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix='/release-dates', tags=['Release Dates'])


@router.get('/{date}', response_model=list[schemas.VideoGame])
async def get_games_by_release_date(date: int, db: Session = Depends(database.get_db)):
    games = db.query(models.VideoGame).filter(models.VideoGame.year == date).all()
    if not games:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No games with release date: {date} were found')
    return games
