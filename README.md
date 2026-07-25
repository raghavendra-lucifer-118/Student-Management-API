# 🎓 Student Management API

A REST API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL** to practice backend development fundamentals.

This project focuses on implementing CRUD operations, database connectivity, dependency injection, and ORM-based database interactions using SQLAlchemy.

---

## 🚀 Features

- Create a student
- View all students
- View a student by ID
- Update student details
- Delete a student
- PostgreSQL database integration
- SQLAlchemy ORM
- Dependency Injection for database sessions

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

---

## 📁 Project Structure

```
student-api/
│
├── main.py          # FastAPI endpoints
├── models.py        # Pydantic request models
├── database.py      # Database configuration and ORM models
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Get all students |
| GET | `/students/{id}` | Get a student by ID |
| POST | `/student` | Add a new student |
| PUT | `/student/{id}` | Update a student |
| DELETE | `/student/{id}` | Delete a student |

---

## 🗄️ Database

The project uses PostgreSQL with SQLAlchemy ORM.

Current tables:

### Students

| Column | Type |
|---------|------|
| std_id | Integer |
| std_name | String |
| course_id | Integer (Foreign Key) |

### Courses

| Column | Type |
|---------|------|
| id | Integer |
| course_name | String |

---

## 📚 Concepts Practiced

- REST API development with FastAPI
- CRUD operations
- Request validation using Pydantic
- SQLAlchemy ORM
- PostgreSQL integration
- Database sessions
- Dependency Injection using `Depends()`
- Foreign Keys
- Basic ORM Relationships

---

## ⚙️ Setup

Clone the repository

```bash
git clone <repository-url>
cd student-api
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment (Windows)

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Update the PostgreSQL connection string in `database.py` if required.

Run the application

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🎯 Purpose

This project was built as a learning exercise to understand how FastAPI communicates with PostgreSQL using SQLAlchemy ORM, while practicing backend architecture and RESTful API development.