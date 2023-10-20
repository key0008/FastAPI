from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship

from api.db import Base
from datetime import date

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, nullable=False, primary_key=True)
    user_name = Column(String(1024), nullable=False)
    
    task = relationship("Task", back_populates="user", cascade="delete")

class Task(Base):
    __tablename__ = "tasks"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    
    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    start_expected_date = Column(DATETIME)
    start_date = Column(DATETIME)
    end_expected_date = Column(DATETIME)
    end_date = Column(DATETIME)
    status = Column(Integer)
    
    user = relationship("User", back_populates="task")
    # status = relationship("Status", back_populates="task", cascade="delete")


# class Status(Base):
#     __tablename__ = "status"
    
#     todo = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
#     doing = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
#     done = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    
#     task = relationship("Task", back_populates="status")
    

# class Todo(Base):
#     __tablename__ = "todo"

#     id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

#     task = relationship("Task", back_populates="todo")

# class Doing(Base):
#     __tablename__ = "doing"

#     id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

#     task = relationship("Task", back_populates="doing")

# class Done(Base):
#     __tablename__ = "dones"

#     id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

#     task = relationship("Task", back_populates="done")
