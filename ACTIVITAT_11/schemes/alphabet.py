from typing import List


def letter_schema(letter: tuple) -> dict:
    return {"letter": letter[0]}


def letters_schema(letters: List[tuple]) -> List[dict]:
    return [letter_schema(letter) for letter in letters]
