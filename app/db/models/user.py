from sqlalchemy import Column, Integer, String
# from app.db.base import Base
from app.db.models.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
