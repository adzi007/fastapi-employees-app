from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    email: str
    division_id: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int
    division_name: str
    class Config:
        # orm_mode = True
        from_attributes = True

