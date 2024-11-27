from ACTIVITAT_10.db_connect.db_connect import create_connection
from ACTIVITAT_10.db_utils.create_words_table import create_table
from ACTIVITAT_10.insertDATA.csv_to_db import csv_to_db


def main():
    try:
        connection = create_connection()
        connection.close()
    except Exception as e:
        raise Exception(f"Error al connectar amb la base de dades: {e}")

    try:
        create_table()
    except Exception as e:
        raise Exception(f"Error al crear la taula: {e}")

    try:
        csv_to_db()
    except Exception as e:
        raise Exception(f"Error durant la inserció de dades desde el CSV: {e}")

    print("Procés amb èxit.")


if __name__ == "__main__":
    main()
