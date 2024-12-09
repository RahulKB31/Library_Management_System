# Library Management System API

## Overview
This project is a simple web application that helps manage a library. You can add, view, update, and delete books and members using a REST API built with Flask. It uses SQLite as the database.

## Features

- Add, view, update, and delete books and members
- Optional: Search books by title or author
- Optional: Pagination to limit the number of books shown per page
- Optional: Token-based authentication for security

## How to Set Up

### 1. **Create a Virtual Environment**
First, create a new virtual environment to manage your project dependencies:
```bash
python -m venv app_env
```

Then, activate the environment:
- On Windows:
  ```bash
  app_env\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source app_env/bin/activate
  ```

### 2. **Install Required Libraries**
Install all the libraries needed for the project:
```bash
pip install -r requirements.txt
```

### 3. **Create the Database**
Run the following Python code to create the database:
```bash
python
from app import db
db.create_all()
```

### 4. **Run the Application**
Now, run the application with:
```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000`.

### 5. **Use the API**
You can use tools like Postman or CURL to interact with the API. Below are the available API endpoints.

---

## API Endpoints

### 1. **Add a New Book (POST /book)**
Adds a new book to the library.

#### Request Example:
```json
{
  "title": "Book Title",
  "author": "Book Author",
  "year": 2020
}
```

#### Response:
```json
{
  "message": "Book added successfully!"
}
```

---

### 2. **Get All Books (GET /books)**
Retrieve a list of all books in the library.

#### Response Example:
```json
[
  {
    "id": 1,
    "title": "Book Title",
    "author": "Book Author",
    "year": 2020
  },
  ...
]
```

---

### 3. **Update a Book (PUT /book/{id})**
Update the details of an existing book.

#### Request Example:
```json
{
  "title": "Updated Title",
  "author": "Updated Author",
  "year": 2021
}
```

#### Response:
```json
{
  "message": "Book updated successfully!"
}
```

---

### 4. **Delete a Book (DELETE /book/{id})**
Delete a book from the library by ID.

#### Response:
```json
{
  "message": "Book deleted successfully!"
}
```

---

### 5. **Add a New Member (POST /member)**
Add a new member to the library.

#### Request Example:
```json
{
  "name": "Member Name",
  "email": "member@example.com"
}
```

#### Response:
```json
{
  "message": "Member added successfully!"
}
```

---

### 6. **Get All Members (GET /members)**
Retrieve a list of all members.

#### Response Example:
```json
[
  {
    "id": 1,
    "name": "Member Name",
    "email": "member@example.com"
  },
  ...
]
```

---

### 7. **Update a Member (PUT /member/{id})**
Update a member's details.

#### Request Example:
```json
{
  "name": "Updated Name",
  "email": "updated@example.com"
}
```

#### Response:
```json
{
  "message": "Member updated successfully!"
}
```

---

### 8. **Delete a Member (DELETE /member/{id})**
Delete a member by ID.

#### Response:
```json
{
  "message": "Member deleted successfully!"
}
```

---

## Design Choices

- **SQLite** is used for simplicity and ease of use.
- **Flask** is used to create the web API because it is lightweight.
- **SQLAlchemy** is used to handle the database.
- **JWT (optional)**: This could be added for authentication if needed.

---

## Assumptions

- No external libraries other than Flask and its dependencies are used.
- The system does not yet include complex features like advanced search or authentication, but these can be added later.

---

## Limitations

- **No user authentication**: There's no login system in place, but you can add JWT authentication if needed.
- **No complex input validation**: Simple validation is used, but more checks can be added.
- **Search and Pagination**: These are optional features and can be added based on future needs.

---

## License

This project is open-source under the MIT License.

