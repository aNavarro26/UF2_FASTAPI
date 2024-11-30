from ACTIVITAT_10.db_connect.db_connect import create_connection
from ACTIVITAT_10.schemas.tematics_sheme import tematics_schema


def get_all_tematics():
    connection = create_connection()
    cursor = connection.cursor()

    try:
        query = "SELECT DISTINCT theme FROM words;"  # per a que sigui única i no hi hagi repetits
        cursor.execute(query)
        results = cursor.fetchall()

        # ja no em fa falta fer el for per transformar els resultats
        return tematics_schema(results)

    except Exception as e:
        print(f"Error al obtenir les tematiques: {e}")
        return []
    finally:
        cursor.close()
        connection.close()


def get_random_word(tematica: str):
    connection = create_connection()
    cursor = connection.cursor()

    try:
        # agafa de manera random una paraula
        query = "SELECT word FROM words WHERE theme = %s ORDER BY RANDOM() LIMIT 1"

        cursor.execute(query, (tematica,))

        result = cursor.fetchone()

        if result:
            return {"word": result[0]}  # si ha trobat que ho retorni en format objecte
        else:
            return None

    except Exception as e:
        print(f"Error al obtenir la paraula amb la temàtica: {tematica}, {e}")
    finally:
        cursor.close()
        connection.close()
