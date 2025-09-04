import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
import crud, schemas, models


def test_create_item(db):
    # Prepare test data using your Pydantic schema
    item_in = schemas.ItemCreate(name="Phone", description="Mobile device", price=500)

    created_item = crud.create_item(db, item_in)

    # Assertions (pytest)
    assert created_item.name == "Phone"
    assert created_item.price == 500
    assert created_item.id is not None