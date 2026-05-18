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

