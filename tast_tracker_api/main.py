# from fastapi import FastAPI, Path #type:ignore
# from pydantic import BaseModel, Field, field_validator, EmailStr #type:ignore 
# from datetime import date



# # dictionaries to store values
# USERS: list = []
# TASKS: list = []


# print(USERS, TASKS)

# # models
# class UserCreate(BaseModel):
#     user_id: int
#     user_name: str = Field(..., min_length=3, max_length=20)
#     email: EmailStr
#     password: str = Field(..., min_length=8, max_length=20)


# class UserRead(BaseModel):
#     user_id: int
#     user_name: str = Field(..., min_length=3, max_length=20)
#     email: EmailStr
#     password: str = Field(..., min_length=8, max_length=20)

# class Task(BaseModel):
#     task_id: int
#     task_name: str
#     task_description: str
#     due_date: str 
    
#     @field_validator("due_date")
#     def valdiate_date(cls, value):
#         if value <= date.today():
#             raise ValueError("Date must be greater than Current Date")

# app = FastAPI()

# @app.post("/users")
# def create_user(user: UserCreate):
#     USER_DICT = {}
#     USER_DICT.user_id = user.user_id
#     USER_DICT.user_name= user.user_name
#     USER_DICT.password = user.password
#     USER_DICT.email = user.email
    
#     USERS.append(USER_DICT)
#     return user



# @app.get("/users/{user_id}")
# def get_user(user_id: int = Path(..., title="the user id to search", gt = 0)):
#     for user in USERS:
#         if user.user_id == user_id:
#             return user

# @app.post("/task")
# def create_task(task: Task):
#     TASKS_DICT = {}
#     TASKS_DICT.task_id = task.task_id
#     TASKS_DICT.task_name = task.task_name
#     TASKS_DICT.task_description = task.task_description
#     TASKS_DICT.due_date = task.due_date
    
#     TASKS.append(TASKS_DICT)
#     return task


# @app.get("/task/{task_id}")
# def get_task(task_id: str):
#     for task in TASKS:
#         if task.task_id == task_id:
#             return task

# @app.put("/task/{task_id}")
# def update_task(task_id: str, task: Task):
#     for task in TASKS:
#         if task.task_id == task_id:
#             task.task_name = task.task_name
#             task.task_description = task.task_description
#             task.due_date = task.due_date
#             return task
                  
from datetime import date
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator

app = FastAPI()

# In-memory databases
users_db = {}
tasks_db = {}
user_id_counter = 1
task_id_counter = 1

# Pydantic Models
class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=20)
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: date
    user_id: int

    @validator('due_date')
    def due_date_must_be_future(cls, v):
        if v < date.today():
            raise ValueError('Due date must be today or later')
        return v

class TaskUpdate(BaseModel):
    status: str

    @validator('status')
    def check_status(cls, v):
        allowed = {"pending", "in progress", "completed"}
        if v not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return v

class Task(TaskCreate):
    id: int
    status: str = "pending"

# User Endpoints
@app.post("/users/", response_model=UserRead)
async def create_user(user: UserCreate):
    global user_id_counter
    user_id = user_id_counter
    users_db[user_id] = {
        "id": user_id,
        "username": user.username,
        "email": user.email,
        "password": user.password
    }
    user_id_counter += 1
    return users_db[user_id]

@app.get("/users/{user_id}", response_model=UserRead)
async def read_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

# Task Endpoints
@app.post("/tasks/", response_model=Task)
async def create_task(task: TaskCreate):
    if task.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    global task_id_counter
    task_id = task_id_counter
    tasks_db[task_id] = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "due_date": task.due_date,
        "user_id": task.user_id,
        "status": "pending"
    }
    task_id_counter += 1
    return tasks_db[task_id]

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks_db[task_id]

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db[task_id]["status"] = task_update.status
    return tasks_db[task_id]

@app.get("/users/{user_id}/tasks", response_model=List[Task])
async def read_user_tasks(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return [task for task in tasks_db.values() if task["user_id"] == user_id]                  
                  