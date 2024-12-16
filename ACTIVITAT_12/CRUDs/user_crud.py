from ACTIVITAT_12.db_connect.db_connect import create_connection
from ACTIVITAT_12.schemes.user_schema import user_schema, users_schema


def get_all_users():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM usuari ORDER BY id ASC;"
    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return users_schema(results)


def get_user_by_id(id: int):
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM usuari WHERE id = %s;"
    cursor.execute(query, (id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return user_schema(result) if result else None


def create_user(user: dict):
    connection = create_connection()
    cursor = connection.cursor()

    query = "INSERT INTO usuari (name) VALUES (%s) RETURNING id;"
    cursor.execute(query, (user["name"],))
    new_id = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return {"id": new_id, "name": user["name"]}


def update_user(id: int, user: dict):
    connection = create_connection()
    cursor = connection.cursor()

    query = "UPDATE usuari SET name = %s WHERE id = %s;"
    cursor.execute(query, (user["name"], id))

    connection.commit()
    cursor.close()
    connection.close()

    return {"id": id, "name": user["name"]}


def delete_user(id: int):
    connection = create_connection()
    cursor = connection.cursor()

    query = "DELETE FROM usuari WHERE id = %s;"
    cursor.execute(query, (id,))

    connection.commit()
    cursor.close()
    connection.close()

    return {"message": f"User with id {id} has been deleted"}
