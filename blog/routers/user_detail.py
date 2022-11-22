from passlib.context import CryptContext
from fastapi import APIRouter,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
import schemas 
import models
from database import get_db
from repository import user_repo




router=APIRouter(
    prefix="/user",
    tags=['Users']
)

pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")
@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    return user_repo.create_user(request,db)

@router.get('/{ids}',response_model=schemas.ShowUser)
def get_user(ids:int,db:Session=Depends(get_db)):
    return  user_repo.get_user(ids,db)