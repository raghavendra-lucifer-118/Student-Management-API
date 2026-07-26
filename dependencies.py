
from database import db_session


def get_db():
    try:
        db = db_session()
        yield db
    finally:
        db.close()   