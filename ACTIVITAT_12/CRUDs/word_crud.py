from ACTIVITAT_12.db_connect.db_connect import create_connection
from ACTIVITAT_12.schemes.word_schema import word_schema, words_schema


# Obtenir totes les paraules
def get_all_words():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM word ORDER BY id ASC;"
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            return words_schema(results)
        return None
    except Exception as e:
        print(f"Error during get_all_words: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Obtenir una paraula per ID
def get_word_by_id(word_id: int):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM word WHERE id = %s;"
        cursor.execute(query, (word_id,))
        result = cursor.fetchone()
        if result:
            return word_schema(result)
        return None
    except Exception as e:
        print(f"Error during get_word_by_id: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Crear una nova paraula
def create_word(word: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "INSERT INTO word (word, theme) VALUES (%s, %s) RETURNING id;"
        cursor.execute(query, (word["word"], word["theme"]))
        new_id = cursor.fetchone()
        connection.commit()
        if new_id:
            return {"id": new_id[0], "word": word["word"], "theme": word["theme"]}
        return None
    except Exception as e:
        print(f"Error during create_word: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Actualitzar una paraula per ID
def update_word(word_id: int, word: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "UPDATE word SET word = %s, theme = %s WHERE id = %s;"
        cursor.execute(query, (word["word"], word["theme"], word_id))
        connection.commit()
        if cursor.rowcount > 0:
            return {"id": word_id, "word": word["word"], "theme": word["theme"]}
        return None
    except Exception as e:
        print(f"Error during update_word: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Eliminar una palabra por ID
def delete_word(word_id: int):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "DELETE FROM word WHERE id = %s;"
        cursor.execute(query, (word_id,))
        connection.commit()
        if cursor.rowcount > 0:
            return {"message": f"Word with ID {word_id} has been deleted."}
        return None
    except Exception as e:
        print(f"Error during delete_word: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
