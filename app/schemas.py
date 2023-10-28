from pydantic import BaseModel


class VideoGame(BaseModel):
    id: int
    name: str
    url: str | None
    year: int | None
    certificate: str | None
    rating: str | None
    plot: str | None
    action: bool | None
    adventure: bool | None
    comedy: bool | None
    crime: bool | None
    family: bool | None
    fantasy: bool | None
    mystery: bool | None
    science_fiction: bool | None
    thriller: bool | None

    class Config:
        from_attributes = True
