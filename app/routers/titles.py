from fastapi import APIRouter, Depends, HTTPException, status
from .. import models, schemas, database
from sqlalchemy.orm import Session

router = APIRouter(prefix='/titles', tags=['Titles'])


@router.get('/', response_model=schemas.VideoGame)
async def get_title(db: Session = Depends(database.get_db)):
    title = db.query(models.VideoGame).first()
    return title
