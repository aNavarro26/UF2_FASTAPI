from ACTIVITAT_12.db_connect.db_connect import create_connection
from ACTIVITAT_12.schemes.attempt_schema import attempts_schema, attempt_schema


# Obtenir tots els registres de attempt
def get_all_attempts():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT id, log_id, letter, is_correct, attempt_number FROM attempt ORDER BY id ASC;"
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            return attempts_schema(results)
        return None
    except Exception as e:
        print(f"Error during get_all_attempts: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Obtenir un intent per ID
def get_attempts_by_log_id(log_id: int):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT id, log_id, letter, is_correct, attempt_number FROM attempt WHERE log_id = %s;"
        cursor.execute(query, (log_id,))
        results = cursor.fetchall()
        if results:
            return attempts_schema(results)
        return None
    except Exception as e:
        print(f"Error during get_attempts_by_log_id: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Crear un nou intent
def create_attempt(attempt: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO attempt (log_id, letter, is_correct, attempt_number)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """
        cursor.execute(
            query,
            (
                attempt["log_id"],
                attempt["letter"],
                attempt["is_correct"],
                attempt["attempt_number"],
            ),
        )
        new_id = cursor.fetchone()
        connection.commit()
        if new_id:
            return {
                "id": new_id[0],
                "log_id": attempt["log_id"],
                "letter": attempt["letter"],
                "is_correct": attempt["is_correct"],
                "attempt_number": attempt["attempt_number"],
            }
        return None
    except Exception as e:
        print(f"Error during create_attempt: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Actualitzar un intent existent
def update_attempt(id: int, attempt: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = """
        UPDATE attempt
        SET log_id = %s, letter = %s, is_correct = %s, attempt_number = %s
        WHERE id = %s;
        """
        cursor.execute(
            query,
            (
                attempt["log_id"],
                attempt["letter"],
                attempt["is_correct"],
                attempt["attempt_number"],
                id,
            ),
        )
        connection.commit()
        if cursor.rowcount > 0:
            return {
                "id": id,
                "log_id": attempt["log_id"],
                "letter": attempt["letter"],
                "is_correct": attempt["is_correct"],
                "attempt_number": attempt["attempt_number"],
            }
        return None
    except Exception as e:
        print(f"Error during update_attempt: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Eliminar un intent
def delete_attempt(id: int):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "DELETE FROM attempt WHERE id = %s;"
        cursor.execute(query, (id,))
        connection.commit()
        if cursor.rowcount > 0:
            return {"message": f"Attempt with id {id} has been deleted"}
        return None
    except Exception as e:
        print(f"Error during delete_attempt: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
