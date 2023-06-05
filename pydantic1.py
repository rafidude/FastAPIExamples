from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


app = FastAPI()

items = {}


@app.post("/items")
async def create_item(item: Item):
    if item.name in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item.name] = item
    print(items)
    return item
