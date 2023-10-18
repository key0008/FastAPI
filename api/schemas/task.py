from typing import Optional
from pydantic import BaseModel, Field

from datetime import date


class TaskBase(BaseModel):
  title: Optional[str] = Field(None, example="クリーニングを取りに行く")
  start_expected_date: Optional[date] = Field(default_factory=date.today)
  start_date: Optional[date] = Field(default_factory=date.today)
  end_expected_date: Optional[date] = Field(default_factory=date.today)
  end_date: Optional[date] = Field(default_factory=date.today)
  
class TaskCreate(TaskBase):
  pass

class TaskCreateResponse(TaskCreate):
  id: int
  
  class Config:
    orm_mode = True
  

class Task(TaskBase):
  """_summary_
  <タスクの中身>
  id: タスクのid
  title: タスク名
  start_expected_date: TODOの開始予定日
  start_date: TODOの開始日
  end_expected_date: TODOの終了予定日
  end_date: TODOの終了日
  
  <フラグ>
  before_work: タスク前
  in_work: タスク中
  done: タスクの終了
  
  Args:
      TaskBase (_type_): _description_
  """
  id: int
  
  before_work: bool = Field(False, description="作業前フラグ")
  in_work: bool = Field(False, description="作業中フラグ")
  done: bool = Field(False, description="作業完了フラグ")
  
  class Config:
    orm_mode = True

