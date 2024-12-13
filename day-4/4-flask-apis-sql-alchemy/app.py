from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models import Employee

app = Flask(__name__)

app.config.from_object('config.Config')

# Initialize database
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{'id': e.id, 'name': e.name, 'position': e.position, 'department': e.department} for e in employees])

@app.route('/employee', methods=['POST'])
def create_employee():
    data = request.json
    if not all(k in data for k in ('name', 'position', 'department')):
        return jsonify({'error': 'Missing fields'}), 400
    new_employee = Employee(name=data['name'], position=data['position'], department=data['department'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee created successfully'}), 201

@app.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify({'id': employee.id, 'name': employee.name, 'position': employee.position, 'department': employee.department})

@app.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.json
    employee.name = data.get('name', employee.name)
    employee.position = data.get('position', employee.position)
    employee.department = data.get('department', employee.department)
    db.session.commit()
    return jsonify({'message': 'Employee updated successfully'})

@app.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({'message': 'Employee deleted successfully'})

if __name__ == "__main__":
    app.run(debug=True)