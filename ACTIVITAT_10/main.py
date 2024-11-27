from fastapi import FastAPI
from typing import List
from ACTIVITAT_10.db_utils.crud import get_all_tematics
from ACTIVITAT_10.schemas.tematics_sheme import Tematic

app = FastAPI()


@app.get("/penjat/tematica/opcions", response_model=List[Tematic])
async def get_tematics():
    return get_all_tematics()

@app.get("/penjat/tematica/{option}")
