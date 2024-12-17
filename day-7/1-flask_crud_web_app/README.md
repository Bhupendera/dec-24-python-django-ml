# Employee CRUD App

## Description
A basic Flask application to perform CRUD operations on an employee table stored in an SQLite database.

## Features
- List employees.
- View employee details.
- Add, edit, and delete employees.
- Flash messages for actions.

## Setup Instructions
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the app:
   ```
   python app.py
   ```
3. Open the app in your browser at `http://127.0.0.1:5000/`.

## File Structure
- `app.py`: Main Flask application.
- `employees.db`: SQLite database file.
- `templates/`: HTML templates for views.
- `static/css/`: Minimal CSS for styling.

## Database Schema
- Table: `employees`
  - `id` (integer, primary key, auto-increment)
  - `name` (text)
  - `email` (text)
  - `phone` (text)
  - `designation` (text)
