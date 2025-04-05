# 📝 NoteHub

**NoteHub** is a simple, RESTful backend service for taking and managing notes, built with Django and Django REST Framework. It supports full CRUD functionality and is designed to be easily integrated with any frontend (e.g., React, Flutter, Vue).

This project is ideal for anyone learning how to build scalable Django APIs using class-based generic views.

---

## ✅ Features

- Full CRUD (Create, Read, Update, Delete) operations for notes
- REST API built using Django REST Framework
- Uses class-based generic views for clean and maintainable code
- Modular project/app structure
- Conda virtual environment support
- SQLite for development (easily swappable for PostgreSQL/MySQL)
- Ready for frontend integration

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/notehub.git
cd notehub
```

### 2. Create and activate a Conda virtual environment

```bash
conda env update -f requirements.yml
conda activate NoteHub
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

---

## 🧱 Project Structure

```
notehub/
├── notes/               # Notes app (models, views, serializers)
├── notes_app/             # Project settings and URLs
├── db.sqlite3           # Development database
├── manage.py            # Django's CLI utility
└── requirements.yml     # Project dependencies
```

---

## 🔌 API Overview

The API is powered by Django REST Framework using **class-based generic views**.

| Method | Endpoint        | Description           |
|--------|------------------|-----------------------|
| GET    | `/api/notes/`    | List all notes        |
| POST   | `/api/notes/`    | Create a new note     |
| GET    | `/api/notes/<id>/` | Retrieve a specific note |
| PUT    | `/api/notes/<id>/` | Update a note         |
| DELETE | `/api/notes/<id>/` | Delete a note         |

> API browsing is supported by DRF’s browsable UI.

---

## 📦 Technologies Used

- Python 
- Django
- Django REST Framework
- SQLite (for development)
- Conda (for environment management)

---

## 🚀 What's Next?

You can extend this project by:
- Adding authentication (JWT or TokenAuth)
- Connecting a frontend (React, Flutter, Vue, etc.)
- Implementing search and filtering
- Adding Swagger/OpenAPI documentation
- Deploying to platforms like Render, Railway, or Heroku

---
