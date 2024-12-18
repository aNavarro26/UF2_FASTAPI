from ACTIVITAT_12.db_connect.db_connect import create_connection
from ACTIVITAT_12.schemes.alphabet_schema import letters_schema, letter_schema


# Obtenir tots els registres de alphabet
def get_all_alphabets():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT id, letter, lang FROM alphabet ORDER BY id ASC;"
        cursor.execute(query)
        results = cursor.fetchall()
        return letters_schema(results)
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Obtenir un alphabet per ID
def get_alphabet_by_lang(lang: str):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT letter, lang FROM alphabet WHERE lang = %s;"
        cursor.execute(query, (lang,))
        result = cursor.fetchone()
        if result:
            return letter_schema(result)
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def create_alphabet(alphabet: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "INSERT INTO alphabet (letter, lang) VALUES (%s, %s) RETURNING id;"  # per no fer un altre consulta i així retornar l'id
        cursor.execute(query, (alphabet["letter"], alphabet["lang"]))
        new_id = cursor.fetchone()[0]
        connection.commit()
        return {"id": new_id, "letter": alphabet["letter"], "lang": alphabet["lang"]}
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def update_alphabet(lang: str, alphabet: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "UPDATE alphabet SET letter = %s WHERE lang = %s;"
        cursor.execute(query, (alphabet["letter"], lang))
        connection.commit()
        return {"lang": lang, "letter": alphabet["letter"]}
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def delete_alphabet(lang: str):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "DELETE FROM alphabet WHERE lang = %s;"
        cursor.execute(query, (lang,))
        connection.commit()
        return {"message": f"Alphabet with lang '{lang}' has been deleted"}
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
