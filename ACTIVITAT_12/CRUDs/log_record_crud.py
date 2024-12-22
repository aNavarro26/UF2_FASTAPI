from ACTIVITAT_12.db_connect.db_connect import create_connection
from ACTIVITAT_12.schemes.log_record_schema import log_records_schema


# Obtenir tots els registres de log
def get_all_log_records():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM log_record ORDER BY log_id ASC;"
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            return log_records_schema(results)
        return None
    except Exception as e:
        print(f"Error during get_all_log_records: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Obtenir registres de log per user_id
def get_log_records_by_user_id(user_id: int):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM log_record WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()
        if results:
            return log_records_schema(results)
        return None
    except Exception as e:
        print(f"Error during get_log_records_by_user_id: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Crear un nou registre de log
def create_log_record(record: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO log_record (ppa, total_games, games_won, best_game_date, best_game_points, user_id)
        VALUES (%s, %s, %s, %s, %s, %s) RETURNING log_id;
        """
        cursor.execute(
            query,
            (
                record["ppa"],
                record["total_games"],
                record["games_won"],
                record["best_game_date"],
                record["best_game_points"],
                record["user_id"],
            ),
        )
        new_id = cursor.fetchone()
        connection.commit()
        if new_id:
            return {
                "log_id": new_id[0],
                "ppa": record["ppa"],
                "total_games": record["total_games"],
                "games_won": record["games_won"],
                "best_game_date": record["best_game_date"],
                "best_game_points": record["best_game_points"],
                "user_id": record["user_id"],
            }
        return None
    except Exception as e:
        print(f"Error during create_log_record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Actualitzar un registre de log existent
def update_log_record(log_id: int, record: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = """
        UPDATE log_record
        SET ppa = %s, total_games = %s, games_won = %s, best_game_date = %s, best_game_points = %s, user_id = %s
        WHERE log_id = %s;
        """
        cursor.execute(
            query,
            (
                record["ppa"],
                record["total_games"],
                record["games_won"],
                record["best_game_date"],
                record["best_game_points"],
                record["user_id"],
                log_id,
            ),
        )
        connection.commit()
        if cursor.rowcount > 0:
            return {
                "log_id": log_id,
                "ppa": record["ppa"],
                "total_games": record["total_games"],
                "games_won": record["games_won"],
                "best_game_date": record["best_game_date"],
                "best_game_points": record["best_game_points"],
                "user_id": record["user_id"],
            }
        return None
    except Exception as e:
        print(f"Error during update_log_record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Eliminar un registre de log per log_id
def delete_log_record(log_id: int):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "DELETE FROM log_record WHERE log_id = %s;"
        cursor.execute(query, (log_id,))
        connection.commit()
        if cursor.rowcount > 0:
            return {"message": f"Log record with log_id {log_id} has been deleted"}
        return None
    except Exception as e:
        print(f"Error during delete_log_record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
