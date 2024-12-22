from typing import List


def user_schema(user: tuple) -> dict:
    return {
        "id": user[0],
        "name": user[1],
    }


def users_schema(users: List[tuple]) -> List[dict]:
    return [user_schema(user) for user in users]
