from fastapi import FastAPI,Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()


origins=["http://localhost:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def index():
    return {'message':'hello world'}
    
@app.post('/user')


