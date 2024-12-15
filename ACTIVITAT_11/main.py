from fastapi import FastAPI
from ACTIVITAT_11.db_utils.attempt_utils import (
    get_total_errors_from_db,
    register_attempt_in_db,
)
from ACTIVITAT_11.schemes.attempt import Attempt
from ACTIVITAT_11.db_utils.alphabet_utils import get_alphabet_from_db
from ACTIVITAT_11.db_utils.player_utils import get_player_stats
from ACTIVITAT_11.db_utils.start_utils import get_start_game_text

app = FastAPI()


# Endpoint per 2 endpoints, per reutilitzar a botó i paraula
@app.get("/penjat/start-game")
async def start_game():
    text = get_start_game_text()
    if text:
        return text
    return {"message": "Text not found"}


# Recollir els errors
@app.get("/penjat/errors/{log_id}")
def get_total_errors(log_id: int):
    total_errors = get_total_errors_from_db(log_id)
    if total_errors is not None:
        return {"log_id": log_id, "total_errors": total_errors}
    return {"message": f"No errors found for log_id {log_id}."}


# Registrar intents
@app.post("/penjat/attempts")
async def post_attempt(attempt: Attempt):
    result = register_attempt_in_db(attempt)
    if result:
        return result
    return {"message": "Failed to register the attempt."}


# Retorna l'alfabet corresponent
@app.get("/penjat/alphabet/{lang}")
async def get_alphabet(lang: str):
    alphabet = get_alphabet_from_db(lang)
    if alphabet:
        return alphabet
    return {"message": f"No alphabet found for the language '{lang}'."}


# Estadístiques Jugador
@app.get("/penjat/game/{log_id}")
async def get_player_info(log_id: int):
    stats = get_player_stats(log_id)
    if stats:
        return stats
    return {"message": "Game not found."}
