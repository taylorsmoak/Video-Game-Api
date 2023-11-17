from fastapi import APIRouter, Depends, HTTPException, status, Query, Path
from .. import models, schemas, database
from sqlalchemy import cast, Float
from sqlalchemy.orm import Session
from typing import Annotated

router = APIRouter(prefix='/games', tags=['Games'])


@router.get('/',
            summary='Filtering games',
            response_model=list[schemas.VideoGame],
            )
async def filter_games(
        name: Annotated[str | None, Query(description='The name of the video game.')] = None,
        date: Annotated[int | None, Query(description='The year the video game was released.')] = None,
        rating: Annotated[int | None, Query(description='The rating (out of 10) of the video game.')] = None,
        genre: Annotated[schemas.genres | None, Query(description='The genre of the video game.')] = None,
        db: Session = Depends(database.get_db)
):
    """
    You can filter video games using the following query parameters. All the parameters are optional. If no parameters
    are set, returns a list of all video games. The parameters are as follows:

    - **name**: A string that appears in the name of the video game.
    - **date**: An integer that represents the year the video game was released.
    - **rating**: An integer that represents the rating (out of 10) of the video game.
    - **genre**: A string that represents the genre of the video game.
    """
    games = db.query(models.VideoGame).order_by(models.VideoGame.name)
    if name:
        games = games.filter(models.VideoGame.name.ilike(f'%{name}%'))
    if date:
        games = games.filter(models.VideoGame.year == date)
    if rating:
        games = games.filter(
            cast(models.VideoGame.rating, Float) >= rating, cast(models.VideoGame.rating, Float) < (rating + 1))
    if genre:
        games = games.filter(getattr(models.VideoGame, genre) == 'True')
    if not games.all():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No games matching the criteria were found')
    return games.all()


@router.get('/{id}',
            summary='Get a single game',
            response_model=schemas.VideoGame)
async def get_single_game(id: Annotated[int, Path(description='The id of the resource')],
                          db: Session = Depends(database.get_db)
                          ):
    """
    Get a single video game by adding the game's id as a path parameter. If you don't know the game's id you can filter
    based on name, release date, rating, and genre using the /games endpoint.

    """
    game = db.query(models.VideoGame).filter(models.VideoGame.id == id).first()
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No game with id: {id} was found')
    return game
