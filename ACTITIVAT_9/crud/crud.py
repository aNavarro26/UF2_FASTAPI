from db_connect.db_connect import create_connection


def read_users():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM users;")
            results = cursor.fetchall()

            cursor.close()
            connection.close()

            users = []

            # itero per cada fila
            for row in results:
                user = {
                    "user_id": row[0],
                    "user_name": row[1],
                    "user_surname": row[2],
                    "user_age": row[3],
                    "user_email": row[4],
                }

                users.append(user)

            return users
        except Exception as e:
            print(f"Error durant l'execució de la consulta: {e}")
            return None
    else:
        print("Connexió fallida")
        return None
