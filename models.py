from pydantic import BaseModel


class Student_model(BaseModel):
    id : int
    name : str
    course_id : int
    

    