from fastapi import FastAPI
from ACTIVITAT_11.db_utils.attempt_utils import (
    get_total_errors_from_db,
    register_attempt_in_db,
)
from ACTIVITAT_11.schemes.attempt import Attempt

app = FastAPI()


@app.get("/penjat/errors/{log_id}")
def get_total_errors(log_id: int):
    total_errors = get_total_errors_from_db(log_id)
    return {"log_id": log_id, "total_errors": total_errors}


# Registrar intents
@app.post("/penjat/attempts", response_model=dict)
async def post_attempt(attempt: Attempt):
    return register_attempt_in_db(attempt)
