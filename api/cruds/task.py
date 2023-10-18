from typing import List, Tuple, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
import api.models.task as task_model
import api.schemas.task as task_schema

from datetime import date

async def get_task(db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
  result: Result = await db.execute(
    select(task_model.Task).filter(task_model.Task.id == task_id)
  )
  task: Optional[Tuple[task_model.Task]] = result.first()
  # 要素が一つであってもtupleで返却されるので一つ目の要素を取り出す
  return task[0] if task is not None else None

async def update_task(
  db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
) -> task_model.Task:
  original.title = task_create.title
  original.start_expected_date = task_create.start_expected_date
  original.start_date = task_create.start_date
  original.end_expected_date = task_create.end_expected_date
  original.end_date = task_create.end_date
  db.add(original)
  await db.commit()
  await db.refresh(original)
  return original

async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
  await db.delete(original)
  await db.commit()
  
    
async def get_tasks_with_done(db: AsyncSession) -> List[Tuple[int, str, date, date, date, date, bool, bool, bool]]:
  result: Result = await(
    db.execute(
      select(
        task_model.Task.id,
        task_model.Task.title,
        task_model.Task.start_expected_date,
        task_model.Task.start_date,
        task_model.Task.end_expected_date,
        task_model.Task.end_date,
        task_model.Before_work.id.isnot(None).label("before_work"),
        task_model.In_work.id.isnot(None).label("in_work"),
        task_model.Done.id.isnot(None).label("done"),
      ).outerjoin(task_model.Done).outerjoin(task_model.Before_work).outerjoin(task_model.In_work)
    )
  )
  return result.all()

async def create_task(
  db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
  task = task_model.Task(**task_create.dict())
  db.add(task)
  await db.commit()
  await db.refresh(task)
  return task