from sqlalchemy.orm import Session, joinedload
from app.db.models.employee import Employee
from app.db.models.division import Division 
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
        return (
            self.db.query(Employee.id,
                Employee.name,
                Employee.email,
                Employee.division_id,
                Division.name.label("division_name")
            )
            .join(Division, Employee.division_id == Division.id)
            .filter(Employee.id == employee_id).first()
        )

    def get_all(self):
        result = (
            self.db.query(
                Employee.id,
                Employee.name,
                Employee.email,
                Employee.division_id,
                Division.name.label("division_name"))
            .join(Division, Employee.division_id == Division.id)
            .all()
        )

        return result
    
    def update_employee(self, employee_id: int, emp: EmployeeCreate):
        employee = self.db.get(Employee, employee_id)
        if not employee:
            return None
        
        employee.name = emp.name
        employee.email = emp.email
        employee.division_id = emp.division_id

        self.db.commit()
        self.db.refresh(employee)

        return employee
    
    def delete_employee(self, emp_id: int):
        employee = self.db.get(Employee, emp_id)
        if not employee:
            return None
        
        self.db.delete(employee)
        self.db.commit()
        return employee