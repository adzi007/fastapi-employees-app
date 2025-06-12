from fastapi import APIRouter, Depends, HTTPException
from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.employee import EmployeeCreate, EmployeeOut
from app.services.employee_service import EmployeeService
from typing import List


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[EmployeeOut])
def get_employee(db: Session = Depends(get_db)):
    return EmployeeService(db).list_employees()

@router.get("/{emp_id}", response_model=EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    return EmployeeService(db).get_employeeById(emp_id)

@router.post("/")
def get_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    EmployeeService(db).create_employee(data)
    return {"message": f"New employee has been created"}

@router.put("/{emp_id}", response_model=EmployeeOut)
def get_employee(emp_id: int, data: EmployeeCreate, db: Session = Depends(get_db)):

    updatedEmployee = EmployeeService(db).update_employee(emp_id, data)

    if updatedEmployee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return updatedEmployee

@router.delete("/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = EmployeeService(db).delete_employee(emp_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return {"message": f"Employee with ID {emp_id} has been deleted"}