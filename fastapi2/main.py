from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException

app = FastAPI()

tasks_db=[]

class TaskCreate(BaseModel):
    title:str
    description:str
    owner:str

class TaskResponse(TaskCreate):
    id:int
    is_completed:bool

@app.get('/')
def home():
    return {"message":"welcome to task manager"}

