from ACTIVITAT_12.db_connect.db_connect import create_connection
from ACTIVITAT_12.schemes.log_record_schema import log_records_schema


# Obtenir tots els registres de log
def get_all_log_records():
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM log_record ORDER BY log_id ASC;"
        cursor.execute(query)
        results = cursor.fetchall()

        return log_records_schema(results)
    except Exception as e:
        print(f"Error during get_all_log_records: {e}")
        return []
    finally:
        if connection:
            cursor.close()
            connection.close()


# Obtenir registres de log per user_id
def get_log_records_by_user_id(user_id: int):
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM log_record WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()

        return log_records_schema(results)
    except Exception as e:
        print(f"Error during get_log_records_by_user_id: {e}")
        return []
    finally:
        if connection:
            cursor.close()
            connection.close()


# Crear un nou registre de log
def create_log_record(record: dict):
    connection = None
    try:
        connection = create_connection()
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
        new_id = cursor.fetchone()[0]
        connection.commit()

        return {"message": "Log record inserted successfully", "log_id": new_id}
    except Exception as e:
        print(f"Error during create_log_record: {e}")
        return {"message": "Failed to insert log record"}
    finally:
        if connection:
            cursor.close()
            connection.close()


# Actualitzar un registre de log existent
def update_log_record(log_id: int, record: dict):
    connection = None
    try:
        connection = create_connection()
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

        return {"message": f"Log record with log_id {log_id} updated successfully"}
    except Exception as e:
        print(f"Error during update_log_record: {e}")
        return {"message": f"Failed to update log record with log_id {log_id}"}
    finally:
        if connection:
            cursor.close()
            connection.close()


# Eliminar un registre de log per log_id
def delete_log_record(log_id: int):
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM log_record WHERE log_id = %s;"
        cursor.execute(query, (log_id,))
        connection.commit()

        return {"message": f"Log record with log_id {log_id} has been deleted"}
    except Exception as e:
        print(f"Error during delete_log_record: {e}")
        return {"message": f"Failed to delete log record with log_id {log_id}"}
    finally:
        if connection:
            cursor.close()
            connection.close()
