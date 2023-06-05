from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    name: str
    price: float


class Category(BaseModel):
    name: str
    items: List[Item]


app = FastAPI()


@app.get("/items/", response_model=List[Item])
async def read_items():
    return [{"name": "Foo", "price": 25.5}, {"name": "Bar", "price": 15.9}]


@app.get("/categories/{category_id}", response_model=Category)
async def read_category(category_id: str):
    return {
        "name": "Fruits",
        "items": [{"name": "Apple", "price": 0.5}, {"name": "Banana", "price": 0.6}],
    }
