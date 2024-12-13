
# Employee CRUD Application

## Features
- Create, Read, Update, Delete employees.
- SQLite database using Flask-SQLAlchemy.
- Swagger UI for API documentation.

## Setup Instructions
1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
   - Linux/Mac: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Initialize the database:
   ```
   flask shell
   from app import db
   db.create_all()
   ```
5. Run the application: `flask run`

## Access Swagger UI
Visit `http://127.0.0.1:5000/swagger` to explore the API.
