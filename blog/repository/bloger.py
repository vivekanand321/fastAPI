from sqlalchemy.orm import Session
import models,schemas
from fastapi import Depends,status,Response,HTTPException
from database import get_db
def get_all(db:Session):
    print("in get_all")
    blogs=db.query(models.Blog).all()
    print(blogs)
    return blogs

def create(request:schemas.Blog,db:Session):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def deleting(id,db:Session):
    blogs=db.query(models.Blog).filter(models.Blog.id==id).first()
    if blogs:
        db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
        db.commit()
        return "done"
    else:
        return "data with {id} does't exist"  

def update(ids,request:schemas.Blog,db:Session):
    blogs=db.query(models.Blog).filter(models.Blog.id==ids)
    if blogs:
        # db.query(models.Blog).filter(models.Blog.id==id).update({'title':'Updated_title'})
        db.query(models.Blog).filter(models.Blog.id==ids).update(request.dict())
        db.commit()
        return 'Updated_successfully'
    else:
        return "Data not existed"

def show(ids,response:Response,db:Session):
    blogs=db.query(models.Blog).filter(models.Blog.id==ids).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog not exist ->{ids}")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f"blog not exist ->{ids}"}
    return blogs        