from sqlalchemy import Column, Integer, String
# from app.db.base import Base
# from app.db.models.base import Base
from app.db.models.base import Base

class Division(Base):
    __tablename__ = "divisions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
