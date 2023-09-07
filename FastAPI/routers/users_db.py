
### Users DB API ###
from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema
from db.client import db_client

router = APIRouter(prefix="/userdb",
                   tags=["/userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

# Inicia el server: uvicorn users:app --reload

users_list = []

@router.get("/")
async def users():
    return users_list

#PATH
@router.get("/{id}")
async def user(id: int):
    return search_user(id)

#Query
@router.get("/")
async def user(id: int):
    return search_user


@router.post("/",response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    #if type(search_user(user.id)) == User:
     #   raise HTTPException(status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
     
    user_dict = dict(user)
    del user_dict["id"]
    
    # Genera y guarda el id
    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.users.find_one({"_id": id}))

    return User(**new_user)

@router.put("/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user

@router.delete("/{id}")
async def user(id: int):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            
    if not found:
        return {"error": "No se ha eliminado el usuario"}
        
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}

