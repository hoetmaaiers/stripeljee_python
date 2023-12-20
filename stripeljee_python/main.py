ebugpyort crud
import debugpy
import models
import schemas
import uvicorn
from database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()


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
def get_comics(db: Session = Depends(get_db)):
    return crud.get_comics(db)


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
async def get_series(db: Session = Depends(get_db)):
    return crud.get_series(db)


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


if __name__ == "__main__":
    # Start the debugger at a specific port (5678 in this example)
    debugpy.listen(5678)
    print("Waiting for debugger to attach...")
    debugpy.wait_for_client()

    uvicorn.run("main:app", reload=True)
