# EWB Library Book Management API

A beginner-friendly REST API for managing a library's books using **FastAPI**, **SQLAlchemy**, and **SQLite**.

## Features

- Create a book
- List all books
- Search by title, author, or category
- Filter by availability
- Retrieve one book by ID
- Update a book
- Delete a book
- Validate request data
- Reject duplicate ISBN values
- Return clear `404` and `409` errors
- Automated API tests

## Requirements

- Python 3.10 or newer
- VS Code (recommended)
- Git (for publishing to GitHub)

## Run locally

Open a terminal in the project root (the folder containing `requirements.txt`).

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

If PowerShell blocks activation, use Command Prompt and run:

```bat
.venv\Scripts\activate.bat
```

Then install dependencies and start Uvicorn as above.

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open these addresses in your browser:

- API home: http://127.0.0.1:8000/
- Health check: http://127.0.0.1:8000/health
- Interactive API docs: http://127.0.0.1:8000/docs

The `library.db` SQLite database is created automatically in the project root when the app starts.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| POST | `/books/` | Create a book |
| GET | `/books/` | List books |
| GET | `/books/{book_id}` | Read one book |
| PUT | `/books/{book_id}` | Replace/update a book |
| DELETE | `/books/{book_id}` | Delete a book |
| GET | `/health` | Health check |

Optional list filters:

- `/books/?title=pragmatic`
- `/books/?author=hunt`
- `/books/?category=Programming`
- `/books/?available=true`

## Example JSON

```json
{
  "title": "The Pragmatic Programmer",
  "author": "Andrew Hunt",
  "isbn": "9780135957059",
  "publication_year": 2019,
  "category": "Programming",
  "available": true
}
```

## Run tests

With the virtual environment active:

```bash
python -m pytest -v
```

## Project structure

```text
EWB_Library_Book_Management_API/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routes.py
├── tests/
│   └── test_books.py
├── .gitignore
├── requirements.txt
└── README.md
```

## GitHub safety note

The `.gitignore` file prevents the local SQLite database and virtual environment from being added to Git. Do not commit passwords, API keys, personal data, or `.env` files.
