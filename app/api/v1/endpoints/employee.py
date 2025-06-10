from fastapi import APIRouter, Depends
from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.employee import EmployeeCreate, EmployeeOut
from app.services.employee_service import EmployeeService


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[EmployeeOut])
def get_employee(db: Session = Depends(get_db)):
    # return {"message": "Test Get Employee"}
    return EmployeeService(db).list_employees()

@router.get("/{emp_id}")
def get_employee(emp_id: int):
    return {"message": f"Working on getting Employee with ID {emp_id}"}

@router.post("/", response_model=EmployeeOut)
def get_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    # return {"message": "Test Post Employee"}
    return EmployeeService(db).create_employee(data)

@router.put("/{emp_id}")
def get_employee(emp_id: int):
    return {"message": f"Test Put Employee with ID {emp_id}"}

@router.delete("/{emp_id}")
def get_employee(emp_id: int):
    return {"message": f"Test Delete Employee with ID {emp_id}"}