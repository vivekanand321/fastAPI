from fastapi import APIRouter,Depends,HTTPException,status
import schemas,database,models,tokenes
from sqlalchemy.orm import Session
from hashing import Hash
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordRequestForm






router=APIRouter(
    tags=['Authentication']
)
# pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")--same code-->using Hash function from hashing.py

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")



    #generating jwt_token
    access_token = tokenes.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}

