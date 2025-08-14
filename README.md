### 📦 Verta – Item Management API

A simple FastAPI + PostgreSQL application for managing items.
Built with SQLAlchemy ORM and structured with CRUD logic for clean maintainability.

### 🚀 Features

Create, read, update, and delete items (CRUD).

PostgreSQL database connection with SQLAlchemy.

Clean project structure with schemas, crud, and database modules.

Built using FastAPI

### 🛠️ Tech Stack

⚡ FastAPI – High-performance Python web framework.

🐘 PostgreSQL – Relational database.

🧾 SQLAlchemy – ORM for database operations.

🐍 Python 3.10+ – Programming language.

🛡️ Pydantic – Data validation and settings management.

### ⚙️ Installation & Setup
## 1️⃣ Clone the repository

```
git clone https://github.com/RalitsaTerzieva/verta
cd verta
```

## 2️⃣ Create a virtual environment

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate
```

## 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

## 4️⃣ Configure the database

Edit database.py with your PostgreSQL credentials:

```
DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydb"
```

## 5️⃣ Run the application

```
uvicorn main:app --reload
```

### 🧪 Example Requests
## ➕ Create an Item

```
curl -X POST "http://127.0.0.1:8000/items/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Laptop", "description": "Workstation", "price": 1200}'

```

## Response

```
{
  "name": "Laptop",
  "description": "Workstation",
  "price": 1200.0,
  "on_offer": false,
  "id": 2
}
```

## 📋 List Items

```
curl -X GET "http://127.0.0.1:8000/items-list/"
```

## Response

```
[
  {
  "name": "Laptop",
  "description": "Workstation",
  "price": 1200.0,
  "on_offer": false,
  "id": 2
}
]
```