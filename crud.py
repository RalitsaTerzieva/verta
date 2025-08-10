from typing import List, Optional
from database import db
from schemas import ItemCreate, ItemUpdate

def create_item(item: ItemCreate):
    return db.add_item(item.dict())

def get_item(item_id: int):
    return db.get_item(item_id)

def update_item(item_id: int, item_update: ItemUpdate):
    update_data = item_update.dict(exclude_unset=True)
    return db.update_item(item_id, update_data)

def delete_item(item_id: int):
    return db.delete_item(item_id)

def list_items(skip: int = 0, limit: int = 10):
    return db.list_items(skip, limit)
