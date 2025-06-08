from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.api.v1.router import api_router

app = FastAPI(title="Employee Management API")

app.include_router(api_router, prefix="/api/v1")

class Item(BaseModel):
    text: str
    is_done: bool = False

items = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee Management API"}

@app.post("/items")
def create_item(item: Item) -> Item:
    items.append(item)
    return item

@app.get("/items", response_model=list[Item])
def get_items(limit: int = 10) -> list:
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="item not exist")