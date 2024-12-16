from ACTIVITAT_12.db_connect.db_connect import create_connection
from ACTIVITAT_12.schemes.attempt_schema import attempts_schema


def get_all_attempts():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT id, log_id, letter, is_correct, attempt_number FROM attempt ORDER BY id ASC;"
    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return attempts_schema(results)


def get_attempts_by_log_id(log_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT id, log_id, letter, is_correct, attempt_number FROM attempt WHERE log_id = %s;"
    cursor.execute(query, (log_id,))
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return attempts_schema(results)


def create_attempt(attempt: dict):
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
    cursor.close()
    connection.close()

    return {
        "id": new_id,
        "log_id": attempt["log_id"],
        "letter": attempt["letter"],
        "is_correct": attempt["is_correct"],
        "attempt_number": attempt["attempt_number"],
    }


def delete_attempt(id: int):
    connection = create_connection()
    cursor = connection.cursor()

    query = "DELETE FROM attempt WHERE id = %s;"
    cursor.execute(query, (id,))

    connection.commit()
    cursor.close()
    connection.close()

    return {"message": f"Attempt with id {id} has been deleted"}
