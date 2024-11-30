from pydantic import BaseModel
from typing import List


class Tematic(BaseModel):
    option: str


# transformo la tupla a un diccionari amb el format que li indico
def tematic_schema(tematic: tuple) -> dict:
    return {"option": tematic[0]}


# trasnforma de llista de tuplas a llista de diccionaris
def tematics_schema(tematics: List[tuple]) -> List[dict]:
    return [tematic_schema(tematic) for tematic in tematics]
