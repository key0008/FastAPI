from fastapi import FastAPI
from api.routers import task, done, before_work, in_work

app = FastAPI()

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)
app.include_router(before_work.router)
app.include_router(in_work.router)

