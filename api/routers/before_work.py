from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.done as done_schema
import api.cruds.done as done_crud
from api.db import get_db

router = APIRouter()

# タスクの作業前フラグ before_work->true
@router.put("/tasks/{task_id}/before_work", response_model = done_schema.DoneResponse)
async def mark_task_as_before_work(task_id: int, db: AsyncSession = Depends(get_db)):
    before_work = await done_crud.get_before_work(db, task_id = task_id)
    if before_work is not None:
        raise HTTPException(status_code = 400, detail = "Before_work already exists")

    return await done_crud.create_Before_work(db, task_id)

# タスクの作業前フラグの削除 before_work->false
@router.delete("/tasks/{task_id}/before_work", response_model = None)
async def unmark_task_as_before_work(task_id: int, db: AsyncSession = Depends(get_db)):
    before_work = await done_crud.get_before_work(db, task_id = task_id)
    if before_work is None:
        raise HTTPException(status_code = 404, detail = "Before_work not found")

    return await done_crud.delete_before_work(db, original = before_work)