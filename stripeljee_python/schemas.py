from pydantic import BaseModel

from stripeljee_python.models import SerieType


# -------------------------------------------------------------------------------
# Serie schemas
class SerieBase(BaseModel):
    title: str
    type: SerieType

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class SerieCreate(SerieBase):
    pass


class SerieUpdate(SerieBase):
    pass


class Serie(SerieBase):
    id: int

    class Config:
        from_attributes = True


# -------------------------------------------------------------------------------
# Comic schemas
class ComicBase(BaseModel):
    title: str
    serie_number: int
    isbn: str


class ComicCreate(ComicBase):
    serie_id: int
    pass


class ComicUpdate(ComicBase):
    serie_id: int
    pass


class Comic(ComicBase):
    id: int
    serie: Serie

    class Config:
        from_attributes = True
