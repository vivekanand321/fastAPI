import schemas,database,models,oauth2
from fastapi import APIRouter,Depends,status,Response,HTTPException
import schemas 
import models
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from typing import List
from repository import bloger

# from . import database
# from blog.routers import blogging



router=APIRouter(
    prefix="/blog",
    tags=['blog']
)


@router.get('/',response_model=List[schemas.ShowBlog])
def get_blog(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return bloger.get_all(db)
   

@router.post('/',status_code=status.HTTP_201_CREATED )
def create(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return bloger.create(request,db)
    

@router.get('/{ids}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def show(ids,response:Response,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return bloger.show(ids,response,db)

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deleting(id,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return bloger.deleting(id,db)  


@router.put('/{ids}',status_code=status.HTTP_202_ACCEPTED)
def update(ids,request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
   return bloger.update(ids,request,db)

