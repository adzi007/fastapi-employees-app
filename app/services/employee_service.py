from sqlalchemy.orm import Session
from app.schemas.employee import EmployeeCreate, EmployeeOut
from app.db.repositories.employee import EmployeeRepository

class EmployeeService:
    def __init__(self, db: Session):
        self.repo = EmployeeRepository(db)

    def create_employee(self, emp: EmployeeCreate):
        return self.repo.create(emp)
    
    def list_employees(self):
        # return self.repo.get_all()
        # employees = self.repo.get_all()
        # return [EmployeeOut(**employee) for employee in employees]
        return self.repo.get_all()
    
    def get_employeeById(self, emp_id: int):
        return self.repo.get_by_id(emp_id)
    
    def update_employee(self, employee_id: int, emp: EmployeeCreate):
        return self.repo.update_employee(employee_id, emp)
    
    def delete_employee(self, emp_id: int):
        return self.repo.delete_employee(emp_id)
