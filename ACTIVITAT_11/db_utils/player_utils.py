from ACTIVITAT_11.db_connect.db_connect import create_connection
from ACTIVITAT_11.schemes.player_logId import player_stats_schema


def get_player_stats(log_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
    SELECT usuari.name, 
        log_record.ppa, 
        log_record.total_games, 
        log_record.games_won, 
        log_record.best_game_date,
        log_record.best_game_points
    FROM usuari 
    JOIN log_record ON usuari.id = log_record.user_id
    WHERE log_record.log_id = %s;
    """

    cursor.execute(query, (log_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return player_stats_schema(result)
    return None
