from fastapi import FastAPI, HTTPException
from models import User, UserUpdateRequest
from typing import List
from uuid import UUID

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("80ef3c9c-77c9-4ff8-b7b2-8aba7af864e2"),
        username="Shubham",
        phone=1234567890,
        email="abc@fastapi.com",
        address="Texas, United States"
        ),
    User(
        id=UUID("216e96f8-ebeb-40f6-a966-1d343adcab38"),
        username="Peaky",
        phone=9841237890,
        email="xyz@fastapi.com",
        address="Virginia, United States"
        )

]

@app.get("/")
async def root():
    return {"Hello": "Shubham Shrivastava"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;    

@app.post("/api/v1/users")  
async def register_user(user: User):
    db.append(user) 
    return {"id": user.id} 

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exits."
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.username is not None:
                user.username == user_update.username 
            if user_update.phone is not None:
                user.phone == user_update.phone 
            if user_update.email is not None:
                user.email == user_update.email 
            if user_update.address is not None:
                user.address == user_update.address
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exits."
    )    