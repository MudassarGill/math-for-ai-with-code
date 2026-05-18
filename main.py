from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class Item(BaseModel):
    name:str
    price:float
    tax:float=None
@app.post('/item')
async def create_item(item:Item):
    if item.tax:
        price_with_tax=item.price+item.tax
    return {
        "name":item.name,
        "price":item.price,
        "tax":item.tax,
        "price_with_tax":price_with_tax
    }
@app.get('/')
def read_root():
    return {"message": "Hello World"}