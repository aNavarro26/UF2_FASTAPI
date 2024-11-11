from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{users_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}
