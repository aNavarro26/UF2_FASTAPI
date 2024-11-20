from fastapi import FastAPI
from db_connect import create_connection
from pydantic import BaseModel
from typing import List

app = FastAPI()


class UserSchema(BaseModel):
    user_id: int
    user_name: str
    user_surname: str
    user_age: int
    user_email: str


@app.get("/users/", response_model=List[UserSchema])
async def read_users():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM users;")
            results = cursor.fetchall()

            cursor.close()
            connection.close()

            users = []

            # per cada fila en el resultat de la consulta que agafa tots itero per afegir-ho a la llista
            # que he fet per a després poder fer return d'aquesta que guardo cada resultat en forma d'objecte json
            for row in results:
                user = {
                    "user_id": row[0],
                    "user_name": row[1],
                    "user_surname": row[2],
                    "user_age": row[3],
                    "user_email": row[4],
                }

                users.append(user)

            return users
        except Exception as e:
            return {"status": "Error durant l'execució de la consulta", "error": str(e)}
    else:
        return {"status": "Connexió fallida"}
