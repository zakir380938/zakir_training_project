from database import base
from sqlalchemy import Column, String
class Student(base):
    __tablename__="students"
    __table_arg__={"schema": "training"}
    id = Column(int, primary_key= True, autoincrement=True)
    name = Column(String(50))
