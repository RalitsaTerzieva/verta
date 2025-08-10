from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import schemas, crud

app = FastAPI(title="Item Management API")

# Enable CORS for local frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/items", response_model=schemas.Item, status_code=201)
async def create_item(item: schemas.ItemCreate):
    return crud.create_item(item)

@app.get("/items/", response_model=List[schemas.Item])
async def read_items(skip: int = 0, limit: int = Query(10, le=100)):
    return crud.list_items(skip=skip, limit=limit)

@app.get("/items/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int):
    item = crud.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.patch("/items/{item_id}", response_model=schemas.Item)
async def update_item(item_id: int, item_update: schemas.ItemUpdate):
    item = crud.update_item(item_id, item_update)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    item = crud.delete_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")