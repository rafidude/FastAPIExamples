from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, PositiveInt
from typing import List


class Item(BaseModel):
    name: str
    tags: List[str]


class Order(BaseModel):
    items: List[Item]


class User(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt


app = FastAPI()


@app.post("/orders/")
async def create_order(order: Order):
    return order


@app.post("/users/")
async def create_user(user: User):
    return user


# {"items": [{"name": "Foo", "tags":
#   ["tag1", "tag2"]},
# {"name": "Bar", "tags": ["tag3"]}]}
# curl -X 'POST' \
#   'http://0.0.0.0:8000/orders/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "items": [
#     {
#       "name": "foo",
#       "tags": [
#         "tag1", "tag2"
#       ]
#     },
#     {
#       "name": "bar",
#       "tags": [
#         "tag3"
#       ]
#     }
#   ]
# }'
# curl -X 'POST' \
#   'http://0.0.0.0:8000/orders/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{"name": "Alice",
# "email": "alice@example.com",
# "age": 25
# }'
