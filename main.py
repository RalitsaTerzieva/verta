from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
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