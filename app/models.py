from .database import Base
from sqlalchemy import Column, Integer, String, Boolean


class VideoGame(Base):
    __tablename__ = 'videogames'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    url = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    certificate = Column(String, nullable=True)
    rating = Column(String, nullable=True)
    plot = Column(String, nullable=True)
    action = Column(Boolean, nullable=True)
    adventure = Column(Boolean, nullable=True)
    comedy = Column(Boolean, nullable=True)
    crime = Column(Boolean, nullable=True)
    family = Column(Boolean, nullable=True)
    fantasy = Column(Boolean, nullable=True)
    mystery = Column(Boolean, nullable=True)
    science_fiction = Column(Boolean, nullable=True)
    thriller = Column(Boolean, nullable=True)
