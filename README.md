# Backend Project 2 – Database Integration (CRUD)

A REST API built with Python, Flask, Flask-SQLAlchemy, and SQLite to demonstrate database integration and complete CRUD operations.

This project was developed as part of my Backend Development Internship at Decode Labs.

## 📌 Project Overview

This project extends REST API fundamentals by connecting a Flask API to a database for persistent data storage.

The API allows users to be:

- Created
- Retrieved
- Updated
- Deleted

It also includes validation to prevent duplicate email entries.

## Features

- REST API built using Flask
- SQLite database integration
- SQLAlchemy ORM
- User data persistence
- Complete CRUD operations
- Input validation
- Duplicate email prevention
- Structured JSON responses
- HTTP status codes for success and errors

## 🛠️ Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- REST API
- Git & GitHub

## 🗄️ User Schema

Each user contains:

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Unique user ID |
| `name` | String | User name |
| `course` | String | Course name |
| `email` | String | Unique email address |

The `id` field is the primary key, while `email` is unique to prevent duplicate entries.

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users` | Create a new user |
| GET | `/users` | Retrieve all users |
| GET | `/users/<id>` | Retrieve a specific user |
| PUT | `/users/<id>` | Update a user |
| DELETE | `/users/<id>` | Delete a user |

## 📥 Create User

### Request

```json
{
    "name": "Abhishek",
    "course": "Backend Development",
    "email": "abhishek.project2@example.com"
}