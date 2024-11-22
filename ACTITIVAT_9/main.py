from fastapi import FastAPI, HTTPException
from typing import List
from schemas.user_scheme import UserSchema
from crud.crud import read_users

app = FastAPI()


@app.get("/users/", response_model=List[UserSchema])
async def get_users():
    users = read_users()
    if users is None:
        raise HTTPException(status_code=500, detail="No es poden obtenir els usuaris.")
    return users
