from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.models import Student_model , Response_model
from repositories import crud

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("/" , response_model=list[Response_model])
def get_students(db : Session = Depends(get_db)):
   return crud.all_students(db) 


@router.get("/{req_id}" , response_model = Response_model)
def get_single_student(req_id:int , db : Session = Depends(get_db)):
    std =  crud.single_student(req_id , db)
    if std is None:
        raise HTTPException(status_code = 404 , detail= "Student Not Found")
    return std  



@router.post("/" , response_model= Response_model )
def add_student(std : Student_model , db : Session = Depends(get_db)):
    return crud.addition_student(std , db)
    


@router.put("/{req_id}" , response_model= Response_model)
def update_student_info(req_id : int , std : Student_model , db : Session = Depends(get_db)):
    std =  crud.student_updation(req_id , std , db)
    if std is None:
        raise HTTPException(status_code = 404 , detail= "Student Not Found")
    return std    


@router.delete("/{req_id}" , response_model= Response_model)
def delete_student(req_id : int , db : Session = Depends(get_db)):
    std =  crud.deletion_student(req_id , db)
    if std is None:
        raise HTTPException(status_code = 404 , detail= "Student Not Found")
    return std   
        
        
  