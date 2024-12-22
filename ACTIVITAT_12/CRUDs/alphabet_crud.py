from ACTIVITAT_12.db_connect.db_connect import create_connection
from ACTIVITAT_12.schemes.alphabet_schema import alphabet_schema, alphabets_schema


# Obtenir tots els registres de alphabet
def get_all_alphabets():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT id, letter, lang FROM alphabet ORDER BY id ASC;"
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            return alphabets_schema(results)
        return None
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
        query = "SELECT id, letter, lang FROM alphabet WHERE LOWER(TRIM(lang)) = LOWER(TRIM(%s));"
        cursor.execute(query, (lang,))
        result = cursor.fetchone()
        if result:
            return alphabet_schema(result)
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Crear un nou alphabet
def create_alphabet(alphabet: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "INSERT INTO alphabet (letter, lang) VALUES (%s, %s) RETURNING id;"  # per no fer un altre consulta i així retornar l'id
        cursor.execute(query, (alphabet["letter"], alphabet["lang"]))
        new_id = cursor.fetchone()
        connection.commit()
        if new_id:
            return {
                "id": new_id[0],
                "letter": alphabet["letter"],
                "lang": alphabet["lang"],
            }
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Actualitzar un alphabet
def update_alphabet(lang: str, alphabet: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "UPDATE alphabet SET letter = %s WHERE lang = %s;"
        cursor.execute(query, (alphabet["letter"], lang))
        connection.commit()
        if cursor.rowcount > 0:  # si ha sigut modificat
            return {"lang": lang, "letter": alphabet["letter"]}
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Eliminar un alphabet
def delete_alphabet(lang: str):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "DELETE FROM alphabet WHERE lang = %s;"
        cursor.execute(query, (lang,))
        connection.commit()
        if cursor.rowcount > 0:
            return {"message": f"Alphabet with lang '{lang}' has been deleted"}
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
