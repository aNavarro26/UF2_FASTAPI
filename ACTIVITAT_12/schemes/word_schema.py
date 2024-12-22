from typing import List


def word_schema(record: tuple) -> dict:
    return {
        "id": record[0],
        "word": record[1],
        "theme": record[2],
    }


def words_schema(records: List[tuple]) -> List[dict]:
    return [word_schema(record) for record in records]
