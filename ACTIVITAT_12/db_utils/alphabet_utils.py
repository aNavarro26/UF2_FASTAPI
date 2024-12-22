from ACTIVITAT_11.db_connect.db_connect import create_connection
from ACTIVITAT_11.schemes.alphabet import letters_schema


def get_alphabet_from_db(lang: str):
    connection = create_connection()
    cursor = connection.cursor()

    # es consulta segons l'idioma sol·licitat
    query = "SELECT letter FROM alphabet WHERE lang = %s;"
    cursor.execute(query, (lang,))
    result = cursor.fetchall()

    # Tuplas a diccionaris usant letters_schema
    alphabet = letters_schema(result)

    cursor.close()
    connection.close()

    return alphabet
