# from __future__ import annotations

from pydantic import BaseModel


# -------------------------------------------------------------------------------
# Serie schemas
class SerieBase(BaseModel):
    title: str


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
