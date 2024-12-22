from ACTIVITAT_11.db_connect.db_connect import create_connection


def get_player_stats(player_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
    SELECT usuari.name, 
           log_record.total_games, 
           log_record.games_won, 
           log_record.best_game, 
           log_record.ppa
    FROM usuari 
    JOIN log_record ON usuari.id = log_record.user_id
    WHERE usuari.id = %s;
    """

    cursor.execute(query, (player_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return {
            "player_name": result[0],
            "total_games": result[1],
            "games_won": result[2],
            "best_game": result[3],
            "best_game_points": result[4],
        }
    return None
