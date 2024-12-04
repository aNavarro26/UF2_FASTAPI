from fastapi import FastAPI, HTTPException
from typing import List


app = FastAPI()


@app.get("/penjat/start_game", response_model=List[dict])
async def get_start_game():
    return get_button_text()


@app.get("/penjat/secret_word", response_model=List[dict])
async def secretWord():
    return get_secret_word()


@app.get("/penjat/attempts", response_model=List[dict])
async def attempts():
    return get_attempts()


@app.get("/penjat/alphabet", response_model=List[dict])
async def alphabet():
    return get_alphabet()


@app.get("/penjat/stats", response_model=List[dict])
async def stats():
    return get_stats()
