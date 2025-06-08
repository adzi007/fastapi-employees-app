from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_employee():
    return {"message": "Test Get Employee"}

@router.get("/{emp_id}")
def get_employee(emp_id: int):
    return {"message": f"Test Get Employee with ID {emp_id}"}

@router.post("/")
def get_employee():
    return {"message": "Test Post Employee"}

@router.put("/{emp_id}")
def get_employee(emp_id: int):
    return {"message": f"Test Put Employee with ID {emp_id}"}

@router.delete("/{emp_id}")
def get_employee(emp_id: int):
    return {"message": f"Test Delete Employee with ID {emp_id}"}