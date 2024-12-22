from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PlayerStats(BaseModel):
    player_name: str
    total_games: int
    games_won: int
    best_game: Optional[datetime]
    best_game_points: int


""" def player_stats_schema(player: tuple) -> dict:
    return {
        "player_name": player[0],
        "total_games": player[1],
        "games_won": player[2],
        "best_game": player[3],
        "best_game_points": player[4],
    }


def player_stats_list_schema(players: List[tuple]) -> List[dict]:
    return [player_stats_schema(player) for player in players]
"""
