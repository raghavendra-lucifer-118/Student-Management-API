from fastapi import FastAPI , Depends
from models import Student_model
from database import db_session , Student_table 
from sqlalchemy.orm import  Session


app = FastAPI()

def get_db():
    try:
        db = db_session()
        yield db
    finally:
        db.close()    



@app.get("/students")
def get_students(db : Session = Depends(get_db)):
    students = db.query(Student_table).all()
    return students


@app.get("/students/{req_id}")
def get_student(req_id:int , db : Session = Depends(get_db)):
    student = db.query(Student_table).filter(Student_table.std_id == req_id).first()
    return student

@app.post("/student")
def add_student(std : Student_model , db : Session = Depends(get_db)):
    new_std = Student_table(
    std_id = std.id,
    std_name = std.name,
    course_id = std.course_id
    )
    db.add(new_std) 
    db.commit()


@app.put("/student/{req_id}")
def add_student(req_id : int , std : Student_model , db : Session = Depends(get_db)):
    student = db.query(Student_table).filter(Student_table.std_id == req_id).first()
    if student is None:
        return "Student not found"
    else:
        student.std_id    = std.id
        student.std_name  = std.name
        student.course_id = std.course_id
        db.commit()
        


@app.delete("/student/{req_id}")
def add_student(req_id : int , db : Session = Depends(get_db)):
    student = db.query(Student_table).filter(Student_table.std_id == req_id).first()
    if student is None:
            return "Student not found"
    else:
        db.delete(student) 
        db.commit()

    