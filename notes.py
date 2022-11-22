'''
we call pydantic model as schema in fastAPI  and sqlalchemy model is known as  model.
in fastapi for database connection we need sqlalchemy there is ceratin line like engine,databae_url,sessions are needed.
for database fields we need models.each model inherits Base from database.py 
from database.py we importing Base to the models which act as parent for Models.these models contining the fields in database.
in main file final connection happens which is models.Base.metadata.create_all(engine).if table not exist then it will make new one or oerate on existing table.
now we are going to handle situation whe we will get the request.
(1)db:Session=Depends(<function instatiatied with SessionLocal from database.py>) 
(2)going to catch and paste incoming request to instance .
(3)saving that instance to database by db.add(<"instance">).
basically Session=Depends(get_db) is giving the existing forat of database one can create or fetch data after instantiating it let say db.
so db:Session=Depends(get_db).for creation instance of model will added to db.
same for fetching making a query to db.query(<model name>).all().
we can made our status code then in decorator we can write status_code=455.fastAPI gives it own status code feature.
sometime it will hapen that default status code not gave proper status in that case we use custom status code with help of Response. 
for both status and custom staus we can use HTTPException .
for deletion we use ->delete(synchronize_session=False)

for partial updation we use .update after query and with model fields we write the needed updated fields.
for complete update we use .upade(request) or .update(request.dict())
'''

'''
let say we have to show only particular fields when we want our data shown by particular id.
in that case we use response_model.Here in Pydantic Model or Schema we made another class which inherits the existing class(this class inheriting BaseModel).
Now  for accessing and restricting the fields to show we use Config class which contain orm_mode=True this is because we are using sqlalchemy which uses ORM queries so indicating the class through config class that ORM_Mode=true.
for that only we have to make the congfig class.
instead of inheriting existing pydenticclass by second class. if second class is going to inherit BaseModel which is already using by first class and we have to resrict to show only title then in class we write.
title:str 
till now restriction on showing filds is for single element what happen if we are getting all data not contining id.
if same procedure will follows then error will came because it is designed only for single data.for restricting larger data we are going to use List[ShowBase]
List is imported from typinghere it will use while getting all the data.

'''
'''
BaseModel will inherited by schemas and : will used to provide datatype whereas in pydantic model Base is inherited and = is used for assignment of the type of field. 
for encryption or hashing of the password we are going to use passlib library.in there we are going to use CryptContext.adding a line above function where have to apply.
here in requirements we are adding bcrypt as well as passlib.
'''
'''
In swaggerUI we have seen the Default Route,now going to see tags for better structure so we add a parameter tags[<name we want to give for route>].
for relationship within a models we first make a connection with each other trhough relationship keyword than giving and accepting model name and relative name.
Foreign key will added in many column(which will taken as many in One to Many).this is the change in Model .
Now in scheams ,in Many fiels (in One to Many) we put the One's (One to Many) as the datatype.
To show one field to other, in our case User model has blogs which related to Blog models (continng Creator field).here in Blog we add creator as showBlog and in User we add Blogs as List(it is One in One2Many)
'''  
'''
APIRouting ->better structering of the app will gave the better understanding od the application for that we use API routing. 
as earlier we were adding tags to particular decorator now it can be written inside APIRouter.
and changing the fixed user not inside the function.
for making application more optimize we are going to make another folder name repository containing extra code from router files passing the parameter and db through it. 
'''
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
'''
def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception'''

