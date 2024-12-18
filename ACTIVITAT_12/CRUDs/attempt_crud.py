from ACTIVITAT_12.db_connect.db_connect import create_connection
from ACTIVITAT_12.schemes.attempt_schema import attempts_schema


# Obtenir tots els registres de attempt
def get_all_attempts():
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT id, log_id, letter, is_correct, attempt_number FROM attempt ORDER BY id ASC;"
        cursor.execute(query)
        results = cursor.fetchall()

        return attempts_schema(results)
    except Exception as e:
        print(f"Error during get_all_attempts: {e}")
        return []
    finally:
        if connection:
            cursor.close()
            connection.close()


# Obtenir un intent per ID
def get_attempts_by_log_id(log_id: int):
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "SELECT id, log_id, letter, is_correct, attempt_number FROM attempt WHERE log_id = %s;"
        cursor.execute(query, (log_id,))
        results = cursor.fetchall()

        return attempts_schema(results)
    except Exception as e:
        print(f"Error during get_attempts_by_log_id: {e}")
        return []
    finally:
        if connection:
            cursor.close()
            connection.close()


def create_attempt(attempt: dict):
    connection = None
    try:
        connection = create_connection()
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
        new_id = cursor.fetchone()[0]
        connection.commit()

        return {
            "id": new_id,
            "log_id": attempt["log_id"],
            "letter": attempt["letter"],
            "is_correct": attempt["is_correct"],
            "attempt_number": attempt["attempt_number"],
        }
    except Exception as e:
        print(f"Error during create_attempt: {e}")
        return {"message": "Failed to create attempt"}
    finally:
        if connection:
            cursor.close()
            connection.close()


def delete_attempt(id: int):
    connection = None
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "DELETE FROM attempt WHERE id = %s;"
        cursor.execute(query, (id,))
        connection.commit()

        return {"message": f"Attempt with id {id} has been deleted"}
    except Exception as e:
        print(f"Error during delete_attempt: {e}")
        return {"message": f"Failed to delete attempt with id {id}"}
    finally:
        if connection:
            cursor.close()
            connection.close()
