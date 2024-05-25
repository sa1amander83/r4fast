from fastapi import FastAPI, Query, Form
from typing import Optional, Annotated
from datetime import date, time
from pydantic import BaseModel
from fastapi import UploadFile, File
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


@app.get("/logout/")
async def logout():
    pass


class SchemeRegister(BaseModel):
    runner: int
    age: int
    category: str = Query(1, ge1=1, le=3)
    gender: str = Query('М')


@app.post("/register/")
async def register(register: SchemeRegister):
    return 'hello'
    pass


@app.get("profiles/{runner}")
async def say_hello(name: int, date_to, date_from):
    return {"message": f"Hello {name} {date_to} "}


class SchemeRunday(BaseModel):
    distance: float
    run_time: time
    avg_time: time

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}