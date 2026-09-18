# Database Integration (CRUD) REST API

A backend REST API built with **Python, Flask, Flask-SQLAlchemy, and SQLite** as part of the Decode Labs Backend Development Internship.

This project extends REST API fundamentals by adding a database layer for persistent user data and implementing complete **CRUD (Create, Read, Update, Delete)** operations.

##  Features

- RESTful API built with Flask
- SQLite database integration
- SQLAlchemy ORM
- User data persistence
- Create, Read, Update, and Delete operations
- Required-field validation
- Duplicate email prevention
- Error handling with appropriate HTTP status codes
- JSON-based API responses

## 🛠️ Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- REST API
- JSON

## 📋 User Schema

Each user contains:

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Unique user identifier |
| `name` | String | User's name |
| `course` | String | User's course |
| `email` | String | User's email address |

The `email` field is unique to prevent duplicate entries.

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users` | Create a new user |
| GET | `/users` | Retrieve all users |
| PUT | `/users/<id>` | Update an existing user |
| DELETE | `/users/<id>` | Delete a user |

## 📌 Example Request

### Create User

**POST `/users`**

```json
{
    "name": "Abhishek",
    "course": "Backend Development",
    "email": "abhishek@example.com"
}