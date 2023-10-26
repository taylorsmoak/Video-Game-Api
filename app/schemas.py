from pydantic import BaseModel


class VideoGame(BaseModel):
    id: int
    name: str
    url: str
    year: int
    certificate: str
    rating: str
    plot: str
    action: bool
    adventure: bool
    comedy: bool
    crime: bool
    family: bool
    fantasy: bool
    mystery: bool
    science_fiction: bool
    thriller: bool

    class Config:
        orm_mode = True
