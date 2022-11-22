
import schemas,models
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from database import get_db
from passlib.context import CryptContext
from hashing import Hash

def create_user(request:schemas.User,db:Session):
    hashed_pass=Hash.bcrypt(request.password)
    new_user=models.User(name=request.name,email=request.email,password=hashed_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(ids:int,db:Session):
    # print("in user_repo")
    fetched_data=db.query(models.User).filter(models.User.id == ids).first()
    if not fetched_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user not exist ->{ids}")
    return fetched_data    