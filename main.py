from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import schemas, crud
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Item Management API")

@app.post("/items/", response_model=schemas.Item, status_code=201)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/items-list/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = Query(10, le=100), db: Session = Depends(get_db)):
    return crud.list_items(db, skip=skip, limit=limit)

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.patch("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item_update: schemas.ItemUpdate, db: Session = Depends(get_db)):
    item = crud.update_item(db, item_id, item_update)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.delete_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
