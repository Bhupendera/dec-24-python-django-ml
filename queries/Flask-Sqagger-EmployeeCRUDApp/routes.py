from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields
from models import db, Employee

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

employee_model = api.model('Employee', {
    'id': fields.Integer(),
    'name': fields.String(required=True, description='The employee name'),
    'position': fields.String(required=True, description='The employee position'),
    'department': fields.String(required=True, description='The employee department'),
})

@api.route('/employees')
class EmployeeList(Resource):
    @api.marshal_list_with(employee_model)
    def get(self):
        employees = Employee.query.all()
        return employees

    @api.expect(employee_model)
    def post(self):
        data = request.json
        try:
            new_employee = Employee(
                name=data['name'],
                position=data['position'],
                department=data['department']
            )
            db.session.add(new_employee)
            db.session.commit()
            return {"message": "Employee created successfully."}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 400

@api.route('/employees/<int:id>')
class EmployeeDetail(Resource):
    @api.marshal_with(employee_model)
    def get(self, id):
        employee = Employee.query.get_or_404(id)
        return employee

    @api.expect(employee_model)
    def put(self, id):
        data = request.json
        employee = Employee.query.get_or_404(id)
        employee.name = data['name']
        employee.position = data['position']
        employee.department = data['department']
        db.session.commit()
        return {"message": "Employee updated successfully."}

    def delete(self, id):
        employee = Employee.query.get_or_404(id)
        db.session.delete(employee)
        db.session.commit()
        return {"message": "Employee deleted successfully."}