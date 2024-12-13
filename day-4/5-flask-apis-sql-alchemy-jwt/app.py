from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta


app = Flask(__name__)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)

app.config["JWT_SECRET_KEY"] = "your-secret-key"  # Replace with a secure key
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"  # Update if needed

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Define the Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Dummy users for authentication
users = {"admin": "password123"}

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

# Get all employees
@app.route('/employees', methods=['GET'])
@jwt_required()
def get_employees():
    employees = Employee.query.all()
    return jsonify([{
        "id": e.id,
        "name": e.name,
        "position": e.position,
        "department": e.department
    } for e in employees])

# Get employee by ID
@app.route('/employee/<int:id>', methods=['GET'])
@jwt_required()
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify({
        "id": employee.id,
        "name": employee.name,
        "position": employee.position,
        "department": employee.department
    })

# Create a new employee
@app.route('/employee', methods=['POST'])
@jwt_required()
def create_employee():
    data = request.json
    if not all(k in data for k in ("name", "position", "department")):
        return jsonify({"error": "Missing fields"}), 400
    new_employee = Employee(
        name=data["name"], position=data["position"], department=data["department"]
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": "Employee created successfully"}), 201

# Update an employee by ID
@app.route('/employee/<int:id>', methods=['PUT'])
@jwt_required()
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.json
    employee.name = data.get("name", employee.name)
    employee.position = data.get("position", employee.position)
    employee.department = data.get("department", employee.department)
    db.session.commit()
    return jsonify({"message": "Employee updated successfully"})

# Delete an employee by ID
@app.route('/employee/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
