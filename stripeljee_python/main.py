import crud
import debugpy
import schemas
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from stripeljee_python.db import SessionLocal, engine
from stripeljee_python.models import Serie, SerieType

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------------------------------------------------------------
# Comic
@app.get("/comics", response_model=list[schemas.Comic])
def get_comics(offset: int, limit: int, db: Session = Depends(get_db)):
    return crud.get_comics(db, offset=offset, limit=limit)


@app.post("/comics")
def create_comic(
    comic: schemas.ComicCreate, db: Session = Depends(get_db)
) -> schemas.Comic:
    return crud.create_comic(db=db, comic=comic)


@app.put("/comics/{comic_id}", response_model=schemas.Comic)
def update_comic(
    comic_id: int, comic: schemas.ComicUpdate, db: Session = Depends(get_db)
):
    db_comic = crud.update_comic(db=db, comic_id=comic_id, comic_data=comic)
    if db_comic is None:
        raise HTTPException(status_code=404, detail="Comic not found")
    return db_comic


# -------------------------------------------------------------------------------
# Serie
@app.get("/series", response_model=list[schemas.Serie])
async def get_series(offset: int, limit: int, db: Session = Depends(get_db)):
    return crud.get_series(db, offset=offset, limit=limit)


@app.post("/series", response_model=schemas.Serie)
def create_serie(serie: schemas.SerieCreate, db: Session = Depends(get_db)):
    return crud.create_serie(db=db, serie=serie)


@app.put("/series/{serie_id}", response_model=schemas.Serie)
def update_serie(
    serie_id: int, serie: schemas.SerieUpdate, db: Session = Depends(get_db)
):
    db_serie = crud.update_serie(db=db, serie_id=serie_id, serie_data=serie)
    if db_serie is None:
        raise HTTPException(status_code=404, detail="Serie not found")
    return db_serie


@app.get("/series/{serie_id}/comics", response_model=list[schemas.Comic])
def get_comics_for_serie(serie_id: int, db: Session = Depends(get_db)):
    db_serie = crud.get_serie(db=db, serie_id=serie_id)
    if db_serie is None:
        raise HTTPException(status_code=404, detail="Serie not found")
    return crud.get_comics_for_serie(db=db, serie_id=serie_id)


# -------------------------------------------------------------------------------
# Serie type
@app.get("/serie_types", response_model=list[str])
async def get_series_types():
    return [serie_type.value for serie_type in SerieType]


if __name__ == "__main__":
    uvicorn.run(app, reload=True)
