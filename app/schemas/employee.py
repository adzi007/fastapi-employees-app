from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    email: str
    division_id: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int
    class Config:
        orm_mode = True

