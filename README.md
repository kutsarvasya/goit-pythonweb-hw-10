# Contacts API

A simple REST API for managing contacts.  
Built as a homework project using FastAPI and PostgreSQL.

---

## Features

- create a contact
- get list of contacts
- get contact by id
- update contact
- delete contact
- search by first name / last name / email
- get contacts with birthdays in the next 7 days

---

## Tech Stack

- FastAPI
- SQLAlchemy async
- PostgreSQL
- Alembic
- Pydantic
- Poetry

---

## How to run

## 1. Clone the project

```bash
git clone <repo-url>
cd <project-folder>
```

## 2. Install dependencies

```bash
poetry install
```

## 3. Create .env

Create a `.env` file in the project root:

```env
DB_URL=postgresql+asyncpg://postgres:567234@localhost:5432/todo_app
```

## 4. Run PostgreSQL with Docker

```bash
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres
```

If container already exists:

```bash
docker start postgres
```

## 5. Run migrations

```bash
poetry run alembic upgrade head
```

## 6. Start the server

```bash
poetry run uvicorn main:app --reload
```

---

## API Docs

```text
http://127.0.0.1:8000/docs
```

---

## Endpoints

- `GET /api/contacts/` - get all contacts
- `GET /api/contacts/{id}` - get one contact
- `POST /api/contacts/` - create contact
- `PUT /api/contacts/{id}` - update contact
- `DELETE /api/contacts/{id}` - delete contact
- `GET /api/contacts/search/?query=` - search contacts
- `GET /api/contacts/birthdays/` - upcoming birthdays

---

## Example request

```json
{
  "first_name": "Anna",
  "last_name": "Ivanova",
  "email": "anna@example.com",
  "phone": "+31612345678",
  "birthday": "1995-05-10",
  "additional_data": "Friend"
}
```

---

## Project structure

```text
src/
  api/
  repository/
  database/
  conf/
  schemas.py
main.py
```

---

## Notes

- database URL is stored in `.env`
- `.env` is added to `.gitignore`
- async database access is used

---

