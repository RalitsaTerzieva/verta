from fastapi import FastAPI, HTTPException, Query, Depends
import schemas, crud

app = FastAPI(title="Item Management API")

@app.post("/items", response_model=schemas.Item, status_code=201)
async def create_item(item: schemas.ItemCreate):
    return crud.create_item(item)