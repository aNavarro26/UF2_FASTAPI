from typing import List


def log_record_schema(record: tuple) -> dict:
    return {
        "log_id": record[0],
        "ppa": record[1],
        "total_games": record[2],
        "games_won": record[3],
        "best_game": record[4],
        "user_id": record[5],
    }


def log_records_schema(records: List[tuple]) -> List[dict]:
    return [log_record_schema(record) for record in records]
