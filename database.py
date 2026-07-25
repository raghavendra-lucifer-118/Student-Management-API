from sqlalchemy.orm import sessionmaker , relationship , declarative_base
from sqlalchemy import create_engine 
from sqlalchemy import Column , Integer , String ,ForeignKey 
Base = declarative_base()

db_url = "postgresql://postgres:postgreSQL@localhost:5432/database2"
engine = create_engine(db_url)
db_session = sessionmaker(autoflush = False , autocommit = False , bind = engine)


class Student_table(Base):
    __tablename__ = "students"
    std_id = Column(Integer , primary_key=True)
    std_name = Column(String)
    course_id = Column(Integer , ForeignKey("courses.id"))
    courses = relationship("Courses_table")
    
    
class Courses_table(Base):
    __tablename__ = "courses"
    id = Column(Integer ,primary_key=True)    
    course_name = Column(String)
    
    
Base.metadata.create_all(bind=engine)        