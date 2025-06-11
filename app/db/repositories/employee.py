from sqlalchemy.orm import Session
from app.db.models.employee import Employee
from app.schemas.employee import EmployeeCreate

class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, emp: EmployeeCreate):
        employee = Employee(**emp.model_dump())
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee
    
    def get_by_id(self, employee_id: int):
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    def get_all(self):
        return self.db.query(Employee).all()