from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# responds to /items/5?q=somequery
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# /items/?skip=20&limit=10
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


@app.get("/itemso/")
async def read_items_o(q: Optional[str] = None):
    if q:
        return {"query": q}
    else:
        return {"query": "No query"}
