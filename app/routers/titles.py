from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix='/titles', tags=['Titles'])


@router.get('/{title}', response_model=list[schemas.VideoGame])
async def get_games_by_title(title: str, db: Session = Depends(database.get_db)):
    games = db.query(models.VideoGame).order_by(models.VideoGame.name).filter(
        models.VideoGame.name.ilike(f'%{title}%')).all()
    if not games:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No games with {title} in the title were found')
    return games


@router.get('/exact/{title}', response_model=list[schemas.VideoGame])
async def get_games_by_exact_title(title: str, db: Session = Depends(database.get_db)):
    games = db.query(models.VideoGame).order_by(models.VideoGame.year).filter(models.VideoGame.name == title).all()
    if not games:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No games with title: {title} were found')
    return games
