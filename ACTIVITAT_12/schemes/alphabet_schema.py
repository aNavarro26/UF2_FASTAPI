from typing import List


def alphabet_schema(alphabet: tuple) -> dict:
    return {
        "id": alphabet[0],
        "letter": alphabet[1],
        "lang": alphabet[2],
    }


def alphabets_schema(alphabets: List[tuple]) -> List[dict]:
    return [alphabet_schema(alphabet) for alphabet in alphabets]
