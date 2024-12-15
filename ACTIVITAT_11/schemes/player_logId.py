from typing import List


def player_stats_schema(record: tuple) -> dict:
    return {
        "player_name": record[0],
        "ppa": record[1],
        "total_games": record[2],
        "games_won": record[3],
        "best_game": f"{record[4]} - {record[5]} points",
    }


def player_stats_list_schema(records: List[tuple]) -> List[dict]:
    return [player_stats_schema(record) for record in records]
