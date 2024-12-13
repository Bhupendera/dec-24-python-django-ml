python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask run


# Get All Employees
curl -X GET http://127.0.0.1:5000/employees

# Create a New Employee
curl -X POST http://127.0.0.1:5000/employee -H "Content-Type: application/json" -d "{\"name\": \"Amit Gupta\", \"position\": \"Software Engineer\", \"department\": \"Engineering\"}"

# Get a Specific Employee
curl -X GET http://127.0.0.1:5000/employee/1

# Update a Specific Employee
curl -X PUT http://127.0.0.1:5000/employee/2 -H "Content-Type: application/json" -d "{\"name\": \"Atin Kumar\", \"position\": \"Senior Software Engineer\", \"department\": \"Engineering\"}"

# Delete a Specific Employee
curl -X DELETE http://127.0.0.1:5000/employee/1