from fastapi import APIRouter,Depends,HTTPException,status
import schemas,database,models,tokenes
from sqlalchemy.orm import Session
from hashing import Hash
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordRequestForm


'''
there will be use of email as username becoz it is given in standard way of Oath2password request form.
through User mode we are going to accespt the username and password .
so initially the user check will only happen on username which is gmail.
for verification of password will be done using verify function having verify keyword using pwt in hashing.py.
also using pydantic modlels for request schemas.login.
'''
'''
now next thing we have to perform is generating JWT and Returning.
for that we have to install python-jose.
making a file tokenise.py which will handle jwt consequeences having secreet key,duration at which session will last.
here in this file when user will authenticated then we will generate a access key after a susseccfully verifing.
making a tokenes.py(name shold not token{name error}) file which is getting the details(email in our case) base on detail with help of JWT function will generate the access_token .
so in tokenes.py there will secret-key,algorithm,access_token _durability with two functions will exist.
first function is for creating the token and second for verifying the token-> this is used by oauth2.py file for verfication of tokens.

to securing everyAPI we have to pass the incoming token for verification to verification function.

Now we have access_token and we want to secure the APIRoutes for that we make another python file name oauth2.in this file we have a function which ensure the verification of the user .
first it will check is their any exeptions in the way.and pass the incoming token with exception result to tokenes.py/verify_token function there verification happens if all right then 
user will logged in otherwise it will show error. 
'''



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

