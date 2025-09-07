import sys
import os

# Add parent directory to sys.path so Python can find database.py
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
import crud, schemas

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydb_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables in the test DB
Base.metadata.create_all(bind=engine)


@pytest.fixture
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.rollback()  # rollback changes after each test
        db.close()

def test_create_item_with_specific_name_and_price(db):
    # Prepare test data using your Pydantic schema
    item_in = schemas.ItemCreate(name="Phone", description="Mobile device", price=500)

    created_item = crud.create_item(db, item_in)

    assert created_item.name == "Phone"
    assert created_item.price == 500
    assert created_item.id is not None

def test_create_item_with_on_offer_set_to_true(db):
    item_in = schemas.ItemCreate(name="Laptop", description="Workstation", price=1200, on_offer=True)
    created_item = crud.create_item(db, item_in)

    assert created_item.on_offer is True
    assert created_item.name == "Laptop"

def test_create_item_with_no_description(db):
    item_in = schemas.ItemCreate(name="Tablet", description=None, price=300)
    created_item = crud.create_item(db, item_in)

    assert created_item.description is None
    assert created_item.name == "Tablet"

def test_create_item_with_decimal_price(db):
    item_in = schemas.ItemCreate(name="Headphones", description="Noise-cancelling", price=99.99)
    created_item = crud.create_item(db, item_in)

    assert created_item.price == 99.99
    assert created_item.name == "Headphones"

def test_create_multiple_items_have_unique_ids(db):
    item1 = schemas.ItemCreate(name="Item1", description="First item", price=10)
    item2 = schemas.ItemCreate(name="Item2", description="Second item", price=20)

    created1 = crud.create_item(db, item1)
    created2 = crud.create_item(db, item2)

    assert created1.id != created2.id

