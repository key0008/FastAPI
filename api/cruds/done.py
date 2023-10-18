from typing import Tuple, Optional
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model

# -----------------------作業前フラグ Before_work--------------------------------
# 作業前フラグ
async def get_before_work(db: AsyncSession, task_id: int) -> Optional[task_model.Before_work]:
  result: Result = await db.execute(
    select(task_model.Before_work).filter(task_model.Before_work.id == task_id)
  )
  before_work: Optional[Tuple[task_model.Before_work]] = result.first()
  
  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
  return before_work[0] if before_work is not None else None

async def create_before_work(db: AsyncSession, task_id: int) -> task_model.Before_work:
  before_work = task_model.Before_work(id = task_id)
  db.add(before_work)
  await db.commit()
  await db.refresh(before_work)
  return before_work

async def delete_before_work(db: AsyncSession, original: task_model.Before_work) -> None:
  await db.delete(original)
  await db.commit()

# 作業完了フラグ
async def get_before_work(db: AsyncSession, task_id: int) -> Optional[task_model.Before_work]:
  result: Result = await db.execute(
    select(task_model.Before_work).filter(task_model.Before_work.id == task_id)
  )
  before_work: Optional[Tuple[task_model.Before_work]] = result.first()
  
  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
  return before_work[0] if before_work is not None else None

async def create_before_work(db: AsyncSession, task_id: int) -> task_model.Before_work:
  before_work = task_model.Before_work(id = task_id)
  db.add(before_work)
  await db.commit()
  await db.refresh(before_work)
  return before_work

async def delete_before_work(db: AsyncSession, original: task_model.Before_work) -> None:
  await db.delete(original)
  await db.commit()


# --------------作業中フラグ in_work--------------------------
# 作業前フラグ
async def get_in_work(db: AsyncSession, task_id: int) -> Optional[task_model.In_work]:
  result: Result = await db.execute(
    select(task_model.In_work).filter(task_model.In_work.id == task_id)
  )
  in_work: Optional[Tuple[task_model.In_work]] = result.first()
  
  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
  return in_work[0] if in_work is not None else None

async def create_in_work(db: AsyncSession, task_id: int) -> task_model.In_work:
  in_work = task_model.In_work(id = task_id)
  db.add(in_work)
  await db.commit()
  await db.refresh(in_work)
  return in_work

async def delete_in_work(db: AsyncSession, original: task_model.In_work) -> None:
  await db.delete(original)
  await db.commit()

# 作業完了フラグ
async def get_in_work(db: AsyncSession, task_id: int) -> Optional[task_model.In_work]:
  result: Result = await db.execute(
    select(task_model.In_work).filter(task_model.In_work.id == task_id)
  )
  in_work: Optional[Tuple[task_model.In_work]] = result.first()
  
  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
  return in_work[0] if in_work is not None else None

async def create_in_work(db: AsyncSession, task_id: int) -> task_model.In_work:
  in_work = task_model.In_work(id = task_id)
  db.add(in_work)
  await db.commit()
  await db.refresh(in_work)
  return in_work

async def delete_in_work(db: AsyncSession, original: task_model.In_work) -> None:
  await db.delete(original)
  await db.commit()


# --------------作業完了フラグ Done--------------------------
# 作業前フラグ
async def get_done(db: AsyncSession, task_id: int) -> Optional[task_model.Done]:
  result: Result = await db.execute(
    select(task_model.Done).filter(task_model.Done.id == task_id)
  )
  done: Optional[Tuple[task_model.Done]] = result.first()
  
  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
  return done[0] if done is not None else None

async def create_done(db: AsyncSession, task_id: int) -> task_model.Done:
  done = task_model.Done(id = task_id)
  db.add(done)
  await db.commit()
  await db.refresh(done)
  return done

async def delete_done(db: AsyncSession, original: task_model.Done) -> None:
  await db.delete(original)
  await db.commit()

# 作業完了フラグ
async def get_done(db: AsyncSession, task_id: int) -> Optional[task_model.Done]:
  result: Result = await db.execute(
    select(task_model.Done).filter(task_model.Done.id == task_id)
  )
  done: Optional[Tuple[task_model.Done]] = result.first()
  
  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
  return done[0] if done is not None else None

async def create_done(db: AsyncSession, task_id: int) -> task_model.Done:
  done = task_model.Done(id = task_id)
  db.add(done)
  await db.commit()
  await db.refresh(done)
  return done

async def delete_done(db: AsyncSession, original: task_model.Done) -> None:
  await db.delete(original)
  await db.commit()
