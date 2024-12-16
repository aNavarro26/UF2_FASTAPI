from pydantic import BaseModel


class Attempt(BaseModel):
    log_id: int
    letter: str
    is_correct: bool
    attempt_number: int


from typing import List


def attempt_schema(attempt: tuple) -> dict:
    return {
        "id": attempt[0],
        "log_id": attempt[1],
        "letter": attempt[2],
        "is_correct": attempt[3],
        "attempt_number": attempt[4],
    }


def attempts_schema(attempts: List[tuple]) -> List[dict]:
    return [attempt_schema(attempt) for attempt in attempts]
