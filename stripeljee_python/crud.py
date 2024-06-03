import models
import schemas
from pydantic import BaseModel
from sqlalchemy.orm import Session, joinedload


def get_serie(db: Session, serie_id: int):
    return db.query(models.Serie).filter(models.Serie.id == serie_id).first()


def create_serie(
    db: Session,
    serie: schemas.SerieCreate,
):
    db_serie = models.Serie(**serie.model_dump())
    db.add(db_serie)
    db.commit()
    db.refresh(db_serie)
    return db_serie


def update_serie(
    db: Session,
    serie_id: int,
    serie_data: schemas.SerieUpdate,
):
    db_serie = db.query(models.Serie).filter(models.Serie.id == serie_id).first()
    if db_serie is None:
        return None
    for (
        var,
        value,
    ) in serie_data.model_dump().items():
        setattr(db_serie, var, value) if value else None
    db.commit()
    db.refresh(db_serie)
    return db_serie


def get_series(db: Session, offset: int = 0, limit: int = 100):
    # Query to get the total number of rows
    # total_rows = db.query(models.Serie).count()

    # Query to get the paginated results
    series = (
        db.query(models.Serie)
        .order_by(models.Serie.id)
        .offset(offset)
        .limit(limit)
        .all()
    )

    return series
    # return {"data": series, "total": total_rows}


def create_comic(
    db: Session,
    comic: schemas.ComicCreate,
):
    db_comic = models.Comic(**comic.model_dump())
    db.add(db_comic)
    db.commit()
    db.refresh(db_comic)
    return db_comic


def update_comic(
    db: Session,
    comic_id: int,
    comic_data: schemas.ComicUpdate,
):
    db_comic = db.query(models.Comic).filter(models.Comic.id == comic_id).first()
    if db_comic is None:
        return None
    for (
        var,
        value,
    ) in comic_data.model_dump().items():
        setattr(db_comic, var, value) if value else None
    db_comic.commit()
    db.refresh(db_comic)
    return db_comic


def get_comics(
    db: Session,
    offset: int = 0,
    limit: int = 100,
):
    return (
        db.query(models.Comic)
        .options(joinedload(models.Comic.serie))
        .order_by(models.Comic.id)
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_comics_for_serie(
    db: Session, offset: int = 0, limit: int = 100, serie_id: int = None
):
    return (
        db.query(models.Comic)
        .filter(models.Comic.serie_id == serie_id)
        .order_by(models.Comic.id)
        .offset(offset)
        .limit(limit)
        .all()
    )
