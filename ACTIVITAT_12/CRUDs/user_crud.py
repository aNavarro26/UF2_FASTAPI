from ACTIVITAT_12.db_connect.db_connect import create_connection
from ACTIVITAT_12.schemes.user_schema import user_schema, users_schema


# Obtenir tots els registres de usuaris
def get_all_users():
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM usuari ORDER BY id ASC;"
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            return users_schema(results)
        return None
    except Exception as e:
        print(f"Error during get_all_users: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Obtenir un usuari per ID
def get_user_by_id(id: int):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM usuari WHERE id = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        if result:
            return user_schema(result)
        return None
    except Exception as e:
        print(f"Error during get_user_by_id: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Crear un nou usuari
def create_user(user: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "INSERT INTO usuari (name) VALUES (%s) RETURNING id;"
        cursor.execute(query, (user["name"],))
        new_id = cursor.fetchone()
        connection.commit()
        if new_id:
            return {"id": new_id[0], "name": user["name"]}
        return None
    except Exception as e:
        print(f"Error during create_user: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Actualitzar un usuari existent
def update_user(id: int, user: dict):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "UPDATE usuari SET name = %s WHERE id = %s;"
        cursor.execute(query, (user["name"], id))
        connection.commit()
        if cursor.rowcount > 0:
            return {"id": id, "name": user["name"]}
        return None
    except Exception as e:
        print(f"Error during update_user: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Eliminar un usuari
def delete_user(id: int):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        query = "DELETE FROM usuari WHERE id = %s;"
        cursor.execute(query, (id,))
        connection.commit()
        if cursor.rowcount > 0:
            return {"message": f"User with id {id} has been deleted"}
        return None
    except Exception as e:
        print(f"Error during delete_user: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
