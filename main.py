from fastapi import FastAPI , Depends
from models import Student_model
from database import db_session , Student_table  , Courses_table
from sqlalchemy.orm import  Session
from sqlalchemy import select
from routers import students

app = FastAPI()
app.include_router(students.router)
    