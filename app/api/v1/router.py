from fastapi import APIRouter
from .endpoints import employee

api_router = APIRouter()
api_router.include_router(employee.router, prefix="/employees", tags=["Employees"])

