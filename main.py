from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is working!"}

users=[
    {"id":1,"name":"lucky","email":"lucky@gmail.com"},
    {"id":2,"name":"daishu","email":"lucky@gmail.com"},
]
@app.get("/users")
def users():
    return users

@app.get("/users/{id}")
def index(id: int):
    for user in users:
        if user["id"]==id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

class User(BaseModel):
    id:int
    name:str
    email:str

@app.post("/user")
def create_user(user:User):
    for u in users:
        if u["id"]==user.id:
            raise HTTPException(status_code=400,detail="User already exists")
        
    users.append(user.dict())
    return{
        "message":"User added successfully."
    }

@app.delete("/users/{id}")
def del_user(id:int):
    for user in users:
        if user["id"]==id:
            user.remove(user)
    return {"meassge":"User deleted successfully."}