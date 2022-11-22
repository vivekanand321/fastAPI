from pydantic import BaseModel
from typing import List,Optional
class Blog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode=True



class User(BaseModel):
    name:str
    email:str
    password:str
    class Config():
        orm_mode=True

class ShowUser(BaseModel):
    name:str
    email:str
    Blogs:List[Blog]
    class Config():
        orm_mode=True

#earlier we used Blog inside ShowBlog
class ShowBlog(BaseModel):
    title:str
    body:str#if i comment body then in UI only title field will shown.
    creator:ShowUser
    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str
    # class Config():
    #     orm_mode=True


class TokenData(BaseModel):
    email: Optional[str] = None
   

    
