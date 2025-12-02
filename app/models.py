from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, text, BOOLEAN
from . database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    name = Column(String(100), nullable=False)
    description = Column(Text)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement= True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    is_active = Column(BOOLEAN, nullable=False, default=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("now()"))

