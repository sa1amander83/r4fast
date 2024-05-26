from fastapi import FastAPI, Query, Form
from typing import Optional, Annotated
from datetime import date, time
from pydantic import BaseModel
from fastapi import UploadFile, File

app = FastAPI()

from profiles.router import router as router_profile
from users.router import router_auth as router_auth
from users.router import router_users as router_users

app.include_router(router_auth)
app.include_router(router_profile)
app.include_router(router_users)


@app.get("/")
async def root():
    return {"message": "Hello World"}


class SchemeRegister(BaseModel):
    runner: int
    age: int
    category: str = Query(1, ge1=1, le=3)
    gender: str = Query('М')


class SchemeRunday(BaseModel):
    distance: float
    run_time: time
    avg_time: time
