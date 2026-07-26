from pydantic import BaseModel


class Student_model(BaseModel):
    id : int
    name : str
    course_id : int
    

class Response_model(BaseModel):
    std_id : int
    std_name : str
    course_id : int    
    
    class Conifg:
        from_attributes = True