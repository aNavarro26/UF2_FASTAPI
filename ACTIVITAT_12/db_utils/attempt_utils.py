from ACTIVITAT_11.db_connect.db_connect import create_connection
from ACTIVITAT_11.schemes.attempt import Attempt


# Obtenir el número d'errors
def get_total_errors_from_db(log_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT COUNT(*) FROM ATTEMPT WHERE log_id = %s AND is_correct = FALSE;"
    cursor.execute(query, (log_id,))
    # agafo l'únic valor que ve
    total_errors = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return total_errors


# Registrar un nou intent
def register_attempt_in_db(attempt: Attempt):
    connection = create_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO ATTEMPT (log_id, letter, is_correct, attempt_number)
    VALUES (%s, %s, %s, %s);
    """

    cursor.execute(
        query,
        (attempt.log_id, attempt.letter, attempt.is_correct, attempt.attempt_number),
    )

    connection.commit()
    cursor.close()
    connection.close()

    return {"message": "Intent registrat correctament"}
