from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    location: str
    email: str
    phone_number: str = None
    manager_name: str = None


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


@app.post("/users/")
async def create_user(user: User):
    return {"user": user}
