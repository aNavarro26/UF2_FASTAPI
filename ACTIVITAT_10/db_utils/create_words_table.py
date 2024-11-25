from db_connect.db_connect import create_connection


def create_table():
    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS words (
        id SERIAL PRIMARY KEY,
        word TEXT NOT NULL,
        theme TEXT NOT NULL
    );
    """
    )

    connection.commit()

    cursor.close()
    connection.close()


def insert_record(dict_list):
    connection = create_connection()

    cursor = connection.cursor()

    query = "INSERT INTO words(word, theme) VALUES (%s, %s)"

    for item in dict_list:
        cursor.execute(query, (item["word"], item["theme"]))

    connection.commit()

    cursor.close()

    connection.close()
