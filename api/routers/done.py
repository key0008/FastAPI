from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.done as done_schema
import api.cruds.done as done_crud
from api.db import get_db

router = APIRouter()

# -------------------タスク作業前フラグ before_work----------------------------
# タスクの作業前フラグ Before_work->true
@router.put("/tasks/{task_id}/Before_work", response_model = done_schema.DoneResponse)
async def mark_task_as_before_work(task_id: int, db: AsyncSession = Depends(get_db)):
    before_work = await done_crud.get_before_work(db, task_id = task_id)
    if before_work is not None:
        raise HTTPException(status_code = 400, detail = "Before_work already exists")

    return await done_crud.create_before_work(db, task_id)

# タスクの作業前フラグの削除 Before_work->false
@router.delete("/tasks/{task_id}/before_work", response_model = None)
async def unmark_task_as_before_work(task_id: int, db: AsyncSession = Depends(get_db)):
    before_work = await done_crud.get_before_work(db, task_id = task_id)
    if before_work is None:
        raise HTTPException(status_code = 404, detail = "Before_work not found")

    return await done_crud.delete_before_work(db, original = before_work)

# -------------------タスク完了フラグIn_work-----------------------------------
# タスクの作業完了フラグ In_work->true
@router.put("/tasks/{task_id}/in_work", response_model = done_schema.DoneResponse)
async def mark_task_as_in_work(task_id: int, db: AsyncSession = Depends(get_db)):
    in_work = await done_crud.get_in_work(db, task_id = task_id)
    if in_work is not None:
        raise HTTPException(status_code = 400, detail = "In_work already exists")

    return await done_crud.create_in_work(db, task_id)

# タスクの作業完了フラグの削除 In_work->false
@router.delete("/tasks/{task_id}/in_work", response_model = None)
async def unmark_task_as_in_work(task_id: int, db: AsyncSession = Depends(get_db)):
    in_work = await done_crud.get_in_work(db, task_id = task_id)
    if in_work is None:
        raise HTTPException(status_code = 404, detail = "In_work not found")

    return await done_crud.delete_in_work(db, original = in_work)


# -------------------タスク完了フラグDone-----------------------------------
# タスクの作業完了フラグ Done->true
@router.put("/tasks/{task_id}/done", response_model = done_schema.DoneResponse)
async def mark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_crud.get_done(db, task_id = task_id)
    if done is not None:
        raise HTTPException(status_code = 400, detail = "Done already exists")

    return await done_crud.create_done(db, task_id)

# タスクの作業完了フラグの削除 Done->false
@router.delete("/tasks/{task_id}/done", response_model = None)
async def unmark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
    done = await done_crud.get_done(db, task_id = task_id)
    if done is None:
        raise HTTPException(status_code = 404, detail = "Done not found")

    return await done_crud.delete_done(db, original = done)