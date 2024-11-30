from fastapi import FastAPI, HTTPException
from typing import List
from ACTIVITAT_10.db_utils.crud import get_all_tematics, get_random_word
from ACTIVITAT_10.schemas.tematics_sheme import Tematic

app = FastAPI()


@app.get("/penjat/tematica/opcions", response_model=List[Tematic])
async def get_tematics():
    return get_all_tematics()


@app.get("/penjat/tematica/{option}", response_model=List[Tematic])
async def get_tematic_word(option: str):
    result = get_random_word(option)

    if result:
        return [{"option": result["word"]}]
    return []
