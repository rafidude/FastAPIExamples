from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}


# curl -X 'POST' \
#   'http://0.0.0.0:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "string1",
#   "price": 10
# }
