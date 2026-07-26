from database import Student_table
from sqlalchemy.orm import Session
from dependencies import get_db
from models import Student_model



def all_students(db : Session):
    students = db.query(Student_table).all()
    return students

def single_student(req_id:int , db : Session ):
    student = db.query(Student_table).filter(Student_table.std_id == req_id).first()
    return student

def addition_student(std:Student_model , db : Session):
    new_std = Student_table(
        std_id = std.id,
        std_name = std.name,
        course_id = std.course_id
        )
    db.add(new_std) 
    db.commit()
    
def updation_student(req_id : int , std : Student_model , db : Session):
    student = db.query(Student_table).filter(Student_table.std_id == req_id).first()
    if student is None:
        return "Student not found"
    else:
        student.std_name  = std.name
        student.course_id = std.course_id
        db.commit() 
        return student   
    
def deletion_student(req_id : int , db:Session):    
    student = db.query(Student_table).filter(Student_table.std_id == req_id).first()
    if student is None:
        return "Student not found"
    else:
        db.delete(student) 
        db.commit()