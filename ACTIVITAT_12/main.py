from fastapi import FastAPI, HTTPException
from ACTIVITAT_12.CRUDs.alphabet_crud import (
    create_alphabet,
    delete_alphabet,
    get_all_alphabets,
    get_alphabet_by_lang,
    update_alphabet,
)
from ACTIVITAT_12.CRUDs.attempt_crud import (
    get_all_attempts,
    get_attempts_by_log_id,
    create_attempt,
    delete_attempt,
    update_attempt,
)
from ACTIVITAT_12.CRUDs.log_record_crud import (
    create_log_record,
    delete_log_record,
    get_all_log_records,
    get_log_records_by_user_id,
    update_log_record,
)
from ACTIVITAT_12.CRUDs.user_crud import (
    create_user,
    delete_user,
    get_all_users,
    get_user_by_id,
    update_user,
)
from ACTIVITAT_12.CRUDs.word_crud import (
    create_word,
    delete_word,
    get_all_words,
    get_word_by_id,
    update_word,
)
from ACTIVITAT_12.db_utils.alphabet_utils import get_alphabet_from_db
from ACTIVITAT_12.db_utils.attempt_utils import (
    get_total_errors_from_db,
    register_attempt_in_db,
)
from ACTIVITAT_12.db_utils.player_utils import get_player_stats
from ACTIVITAT_12.db_utils.start_utils import get_start_game_text
from ACTIVITAT_12.schemes.attempt_schema import Attempt

app = FastAPI()


# CRUD Alphabet
@app.get("/alphabet")
async def get_all_alphabets_endpoint():
    result = get_all_alphabets()
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve alphabets.")
    return result


@app.get("/alphabet/{lang}")
async def get_alphabet_by_lang_endpoint(lang: str):
    result = get_alphabet_by_lang(lang)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Alphabet for language '{lang}' not found."
        )
    return result


@app.post("/alphabet")
async def create_alphabet_endpoint(alphabet: dict):
    result = create_alphabet(alphabet)
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to create alphabet.")
    return result


@app.put("/alphabet/{lang}")
async def update_alphabet_endpoint(lang: str, alphabet: dict):
    result = update_alphabet(lang, alphabet)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Alphabet for language '{lang}' not found."
        )
    return result


@app.delete("/alphabet/{lang}")
async def delete_alphabet_endpoint(lang: str):
    result = delete_alphabet(lang)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Alphabet for language '{lang}' not found."
        )
    return result


# CRUD Attempt
@app.get("/attempts")
async def get_all_attempts_endpoint():
    result = get_all_attempts()
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve attempts.")
    return result


@app.get("/attempts/{log_id}")
async def get_attempts_by_log_id_endpoint(log_id: int):
    result = get_attempts_by_log_id(log_id)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Attempts for log_id '{log_id}' not found."
        )
    return result


@app.post("/attempts")
async def create_attempt_endpoint(attempt: dict):
    result = create_attempt(attempt)
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to create attempt.")
    return result


@app.put("/attempts/{id}")
async def update_attempt_endpoint(id: int, attempt: dict):
    result = update_attempt(id, attempt)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Attempt with id '{id}' not found."
        )
    return result


@app.delete("/attempts/{id}")
async def delete_attempt_endpoint(id: int):
    result = delete_attempt(id)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Attempt with id '{id}' not found."
        )
    return result


# CRUD Log_Record
@app.get("/log-records")
async def get_all_log_records_endpoint():
    result = get_all_log_records()
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve log records.")
    return result


@app.get("/log-records/{user_id}")
async def get_log_records_by_user_id_endpoint(user_id: int):
    result = get_log_records_by_user_id(user_id)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Log records for user_id '{user_id}' not found."
        )
    return result


@app.post("/log-records")
async def create_log_record_endpoint(record: dict):
    result = create_log_record(record)
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to create log record.")
    return result


@app.put("/log-records/{log_id}")
async def update_log_record_endpoint(log_id: int, record: dict):
    result = update_log_record(log_id, record)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Log record with log_id '{log_id}' not found."
        )
    return result


@app.delete("/log-records/{log_id}")
async def delete_log_record_endpoint(log_id: int):
    result = delete_log_record(log_id)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Log record with log_id '{log_id}' not found."
        )
    return result


# CRUD Users
@app.get("/users")
async def get_all_users_endpoint():
    result = get_all_users()
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve users.")
    return result


@app.get("/users/{id}")
async def get_user_by_id_endpoint(id: int):
    result = get_user_by_id(id)
    if result is None:
        raise HTTPException(status_code=404, detail=f"User with id '{id}' not found.")
    return result


@app.post("/users")
async def create_user_endpoint(user: dict):
    result = create_user(user)
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to create user.")
    return result


@app.put("/users/{id}")
async def update_user_endpoint(id: int, user: dict):
    result = update_user(id, user)
    if result is None:
        raise HTTPException(status_code=404, detail=f"User with id '{id}' not found.")
    return result


@app.delete("/users/{id}")
async def delete_user_endpoint(id: int):
    result = delete_user(id)
    if result is None:
        raise HTTPException(status_code=404, detail=f"User with id '{id}' not found.")
    return result


# CRUD Words
@app.get("/words")
async def get_all_words_endpoint():
    result = get_all_words()
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve words.")
    return result


@app.get("/words/{word_id}")
async def read_word(word_id: int):
    result = get_word_by_id(word_id)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Word with id '{word_id}' not found."
        )
    return result


@app.post("/words")
async def add_word(word: dict):
    result = create_word(word)
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to create word.")
    return result


@app.put("/words/{word_id}")
async def modify_word(word_id: int, word: dict):
    result = update_word(word_id, word)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Word with id '{word_id}' not found."
        )
    return result


@app.delete("/words/{word_id}")
async def remove_word(word_id: int):
    result = delete_word(word_id)
    if result is None:
        raise HTTPException(
            status_code=404, detail=f"Word with id '{word_id}' not found."
        )
    return result


# Endpoints Penjat
@app.get("/penjat/start-game")
async def start_game():
    text = get_start_game_text()
    if text is None:
        raise HTTPException(
            status_code=500, detail="Failed to retrieve start game text."
        )
    return text


@app.get("/penjat/errors/{log_id}")
def get_total_errors(log_id: int):
    total_errors = get_total_errors_from_db(log_id)
    if total_errors is None:
        raise HTTPException(
            status_code=404, detail=f"No errors found for log_id '{log_id}'."
        )
    return {"log_id": log_id, "total_errors": total_errors}


@app.post("/penjat/attempts")
async def post_attempt(attempt: Attempt):
    result = register_attempt_in_db(attempt)
    if result is None:
        raise HTTPException(status_code=500, detail="Failed to register the attempt.")
    return result


@app.get("/penjat/alphabet/{lang}")
async def get_alphabet(lang: str):
    alphabet = get_alphabet_from_db(lang)
    if alphabet is None:
        raise HTTPException(
            status_code=404, detail=f"No alphabet found for language '{lang}'."
        )
    return alphabet


@app.get("/penjat/game/{log_id}")
async def get_player_info(log_id: int):
    stats = get_player_stats(log_id)
    if stats is None:
        raise HTTPException(
            status_code=404, detail=f"Game with log_id '{log_id}' not found."
        )
    return stats
