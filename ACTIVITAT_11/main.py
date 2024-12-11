from fastapi import FastAPI
from typing import List
from ACTIVITAT_11.db_utils.attempt_utils import (
    get_total_errors_from_db,
    register_attempt_in_db,
)
from ACTIVITAT_11.schemes.attempt import Attempt
from ACTIVITAT_11.schemes.player_logId import PlayerStats
from ACTIVITAT_11.db_utils.alphabet_utils import get_alphabet_from_db
from ACTIVITAT_11.db_utils.player_utils import get_player_stats
from ACTIVITAT_11.db_utils.start_utils import get_start_game_text

app = FastAPI()


# Endpoint per 2 endpoints, per reutilitzar a botó i paraula
@app.get("/penjat/start-game")
async def start_game():
    text = get_start_game_text()
    return text


# Recollir els errors
@app.get("/penjat/errors/{log_id}")
def get_total_errors(log_id: int):
    total_errors = get_total_errors_from_db(log_id)
    return {"log_id": log_id, "total_errors": total_errors}


# Registrar intents
@app.post("/penjat/attempts", response_model=dict)
async def post_attempt(attempt: Attempt):
    return register_attempt_in_db(attempt)


# Retorna l'alfabet corresponent
@app.get("/penjat/alphabet/{lang}", response_model=List[dict])
async def get_alphabet(lang: str):
    alphabet = get_alphabet_from_db(lang)
    return alphabet


""" @app.get("/penjat/player/{player_id}", response_model=List[dict])
async def get_player_info(player_id: int):
    stats = get_player_stats(player_id)
    return player_stats_list_schema(stats) """


@app.get("/penjat/player/{player_id}", response_model=PlayerStats)
async def get_player_info(player_id: int):
    stats = get_player_stats(player_id)
    if stats:
        return stats
    return None
