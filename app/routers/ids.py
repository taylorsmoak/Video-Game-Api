from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix='/id', tags=['ID'])


@router.get('/{index}', response_model=schemas.VideoGame)
async def get_game_by_id(index: int, db: Session = Depends(database.get_db)):
    game = db.query(models.VideoGame).filter(models.VideoGame.id == index).first()
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No game with id: {index} was found')
    return game
