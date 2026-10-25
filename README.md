# 📚 Library Book Management API

A RESTful API for managing library books, built using **Python, FastAPI, and SQLite**.

This project demonstrates CRUD operations (Create, Read, Update, and Delete), data validation, database integration, and automated testing.

## ✨ Features

- Add new books to the library.
- View all books.
- Retrieve a book by its ID.
- Update book details.
- Delete books.
- Search and filter books.
- Validate book information.
- Prevent duplicate ISBN numbers.
- Store book records in an SQLite database.
- Run automated tests using pytest.

## 🛠️ Technologies Used

- **Python** — Programming language.
- **FastAPI** — Web API framework.
- **SQLite** — Database.
- **SQLAlchemy** — Database toolkit and ORM.
- **Pydantic** — Data validation.
- **Pytest** — Automated testing.

## 📁 Project Structure

```text
EWB_Library_Book_Management_API/
├── app/
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

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Pavan-Chegu123/ewb-library-book-management-api.git
```

### 2. Open the project folder

```bash
cd ewb-library-book-management-api
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Start the API server

```bash
python -m uvicorn app.main:app --reload
```

### 7. Open the interactive API documentation

Visit:

http://127.0.0.1:8000/docs

You can use this page to explore and test the API endpoints.

## 🧪 Run Tests

With the virtual environment activated, run:

```bash
python -m pytest -v
```

The project includes tests for API health, book CRUD operations, duplicate ISBN validation, and error handling.

## 🎯 Learning Objectives

This project demonstrates practical experience with:

- Building REST APIs using FastAPI.
- Working with databases.
- Validating request data.
- Handling API errors.
- Writing automated tests.
- Using Git and GitHub for version control.

## 👩‍💻 Author

**Pavan Chegu**

GitHub: [Pavan-Chegu123](https://github.com/Pavan-Chegu123)

---

If you find this project useful, feel free to explore the code and learn from it.