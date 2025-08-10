from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    name: str = Field(..., example="My Item")
    description: Optional[str] = Field(None, example="A description of the item")
    price: float = Field(..., gt=0, example=99.99)
    on_offer: Optional[bool] = Field(False, example=True)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    on_offer: Optional[bool] = None

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
