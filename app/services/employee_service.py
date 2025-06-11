from sqlalchemy.orm import Session
from app.schemas.employee import EmployeeCreate
from app.db.repositories.employee import EmployeeRepository

class EmployeeService:
    def __init__(self, db: Session):
        self.repo = EmployeeRepository(db)

    def create_employee(self, emp: EmployeeCreate):
        return self.repo.create(emp)
    
    def list_employees(self):
        return self.repo.get_all()
    
    def get_employeeById(self, emp_id: int):
        return self.repo.get_by_id(emp_id)
