from fastapi import FastAPI, Depends, HTTPException


def get_db():
    db = {"John": "admin", "Anna": "user", "Tom": "user"}
    return db


def get_current_user(db=Depends(get_db)):
    role = db.get(
        "John"
    )  # In a real application, you would get the logged-in user's name from the request.
    if not role:
        raise HTTPException(status_code=404, detail="User not found")
    return ("John", role)


app = FastAPI()


@app.get("/users/me")
def read_current_user(info=Depends(get_current_user)):
    return {"user": info[0], "role": info[1]}
