from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship

from api.db import Base
from datetime import date


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    start_expected_date = Column(DATETIME)
    start_date = Column(DATETIME)
    end_expected_date = Column(DATETIME)
    end_date = Column(DATETIME)
    
    before_work = relationship("Before_work", back_populates="task", cascade="delete")
    in_work = relationship("In_work", back_populates="task", cascade="delete")
    done = relationship("Done", back_populates="task", cascade="delete")
    


class Before_work(Base):
    __tablename__ = "before_work"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task", back_populates="before_work")

class In_work(Base):
    __tablename__ = "in_work"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task", back_populates="in_work")

class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task", back_populates="done")
