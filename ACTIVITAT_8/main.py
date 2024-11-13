from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    location: str
    email: str
    phone_number: Optional[str] = None
    manager_name: Optional[str] = None


@app.get("/users/{user_id}")
async def read_user(user_id: int, response: Response):
    # com si el 42 no existeixi
    if user_id == 42:
        response.status_code = 404
        return {"detail": "User not found"}
    return {"user_id": user_id}
