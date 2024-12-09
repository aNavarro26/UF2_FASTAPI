from pydantic import BaseModel


class Attempt(BaseModel):
    log_id: int
    letter: str
    is_correct: bool
    attempt_number: int
