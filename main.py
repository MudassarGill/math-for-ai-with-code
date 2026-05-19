from fastapi import FastAPI,Depends
from pydantic import BaseModel


app=FastAPI()

def get_message(msg:str):
    return 'Hello from dependencyinjection:'

@app.get('/')
def users(msg = Depends(get_message)):
    return f'{msg}'



