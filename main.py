from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
app=FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id:int):
    await asyncio.sleep(5)
    return {"user_id":user_id}
@app.get("/user_name/{user_name}")
async def get_user_name(user_name:str):
    return user_name

@app.get("/")
async def read_root():
    return {'Massege':'FastAPI is alive'}

@app.get('/users')
async def read_users(skip:int=0,limit:int=10):
    return {'message':f'we have {limit} users starting from {skip}'}


class user(BaseModel):
    name:str
    age:int
    email:str
   

@app.post('/users')
async def create_user(user:user):
    return {'message':f'User {user.name} created'}
    
