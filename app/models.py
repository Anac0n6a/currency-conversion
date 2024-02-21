from sqlalchemy import Column, Integer, String, Float
from database import Base
from datetime import datetime

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String, unique=True)
    rate = Column(Float)
    updated_at = Column(String, default=str(datetime.utcnow()))