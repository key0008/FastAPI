from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.done as done_schema
import api.cruds.done as done_crud
from api.db import get_db

router = APIRouter()


# タスクの作業中フラグ in_work->true
@router.put("/tasks/{task_id}/in_work", response_model = done_schema.DoneResponse)
async def mark_task_as_in_work(task_id: int, db: AsyncSession = Depends(get_db)):
    in_work = await done_crud.get_in_work(db, task_id = task_id)
    if in_work is not None:
        raise HTTPException(status_code = 400, detail = "In_work already exists")

    return await done_crud.create_in_work(db, task_id)

# タスクの作業中フラグの削除 in_work->false
@router.delete("/tasks/{task_id}/in_work", response_model = None)
async def unmark_task_as_in_work(task_id: int, db: AsyncSession = Depends(get_db)):
    in_work = await done_crud.get_in_work(db, task_id = task_id)
    if in_work is None:
        raise HTTPException(status_code = 404, detail = "In_work not found")

    return await done_crud.delete_in_work(db, original = in_work)