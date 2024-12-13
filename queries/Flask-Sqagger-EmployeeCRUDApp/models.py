from app import db

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)

    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department

    def __repr__(self):
        return f"<Employee {self.id} - {self.name}, {self.position}, {self.department}>"
