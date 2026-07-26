from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from database import Student_table
from dependencies import get_db
from models import Student_model
from repositories import crud

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("/")
def get_students(db : Session = Depends(get_db)):
   return  crud.all_students(db)
    


@router.get("/{req_id}")
def get_single_student(req_id:int , db : Session = Depends(get_db)):
    return crud.single_student(req_id , db)



@router.post("/")
def add_student(std : Student_model , db : Session = Depends(get_db)):
    return crud.addition_student(std , db)


@router.put("/{req_id}")
def update_student_info(req_id : int , std : Student_model , db : Session = Depends(get_db)):
    return crud.student_updation(req_id , std , db)
        


@router.delete("/{req_id}")
def delete_student(req_id : int , db : Session = Depends(get_db)):
    return crud.deletion_student(req_id , db)
        
        
  