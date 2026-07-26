from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from database import Student_table
from dependencies import get_db
from models import Student_model


router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("/")
def get_students(db : Session = Depends(get_db)):
    students = db.query(Student_table).all()
    return students


@router.get("/{req_id}")
def get_single_student(req_id:int , db : Session = Depends(get_db)):
    student = db.query(Student_table).filter(Student_table.std_id == req_id).first()
    return student



@router.post("/")
def add_student(std : Student_model , db : Session = Depends(get_db)):
    new_std = Student_table(
    std_id = std.id,
    std_name = std.name,
    course_id = std.course_id
    )
    db.add(new_std) 
    db.commit()


@router.put("/{req_id}")
def update_student_info(req_id : int , std : Student_model , db : Session = Depends(get_db)):
    student = db.query(Student_table).filter(Student_table.std_id == req_id).first()
    if student is None:
        return "Student not found"
    else:
        student.std_name  = std.name
        student.course_id = std.course_id
        db.commit()
        


@router.delete("/{req_id}")
def delete_student(req_id : int , db : Session = Depends(get_db)):
    student = db.query(Student_table).filter(Student_table.std_id == req_id).first()
    if student is None:
            return "Student not found"
    else:
        db.delete(student) 
        db.commit()
        
        
  