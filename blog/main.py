from fastapi import FastAPI,Depends,status,Response,HTTPException
import schemas 
import models
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
# from . import database
# from blog.routers import blogging
from routers import blogging,user_detail,authentication

 

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blogging.router)
app.include_router(user_detail.router)
app.include_router(authentication.router)


#Below Code is when we are not using APIRouting
# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=["Blogs"])
# def create(request:schemas.Blog,db:Session=Depends(get_db)):
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=["Blogs"])
# def get_blog(dbs:Session=Depends(get_db)):
#     blogs=dbs.query(models.Blog).all()#convert it to query 
#     return blogs

# @app.get('/blog/{ids}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog,tags=["Blogs"])
# def show(ids,response:Response,db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).filter(models.Blog.id==ids).first()
#     if not blogs:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog not exist ->{ids}")
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {'detail':f"blog not exist ->{ids}"}
#     return blogs

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
# def deleting(id,db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).filter(models.Blog.id==id).first()
#     if blogs:
#         db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
#         db.commit()
#         return "done"
#     else:
#         return "data with {id} does't exist"    


# @app.put('/blog/{ids}',status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
# def update(ids,request:schemas.Blog,db:Session=Depends(get_db)):
#     blogs=db.query(models.Blog).filter(models.Blog.id==ids)
#     if blogs:
#         # db.query(models.Blog).filter(models.Blog.id==id).update({'title':'Updated_title'})
#         db.query(models.Blog).filter(models.Blog.id==ids).update(request.dict())
#         db.commit()
#         return 'Updated_successfully'
#     else:
#         return "Data not existed"

# pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")
# @app.post('/user',response_model=schemas.ShowUser,tags=["Users"])
# def create_user(request:schemas.User,db:Session=Depends(get_db)):
#     hashed_pass=pwd_cxt.hash(request.password)
#     new_user=models.User(name=request.name,email=request.email,password=hashed_pass)
#     print("--------------------------------------------",new_user.name,new_user.email,new_user.password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{ids}',response_model=schemas.ShowUser,tags=["Users"])
# def get_user(ids:int,db:Session=Depends(get_db)):
#     print("ids is ---------",ids)
#     fetched_data=db.query(models.User).filter(models.User.id == ids)
#     print("fetched data is-----------------------",fetched_data)
#     if not fetched_data:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user not exist ->{ids}")
#     return fetched_data



