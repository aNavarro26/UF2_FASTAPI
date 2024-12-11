from ACTIVITAT_11.db_connect.db_connect import create_connection


def get_start_game_text():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT word FROM word WHERE word = 'Començar Partida';"
    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return {"text": result[0]}
    return {"text": None}
