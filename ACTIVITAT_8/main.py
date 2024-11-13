from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# com si fos una bdd per trobar registres
items = {"foo": "The Foo Wrestlers"}


class User(BaseModel):
    name: str
    age: int
    location: str
    email: str
    phone_number: Optional[str] = None
    manager_name: Optional[str] = None


# HTTExeption
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


# Response
@app.get("/users/{user_id}")
async def read_user(user_id: int, response: Response):
    # si es posa més de 10 es com si no existeix
    if user_id > 10:
        response.status_code = 404
        return {"detail": "User not found"}
    return {"user_id": user_id}


# POST
@app.post("/users/")
async def create_user(user: User):
    return {"user": user}
