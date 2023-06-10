from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/hello", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Hello, FastAPI"}
    )


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items/")
def create_item(item: Item):
    return item
