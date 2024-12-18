import psycopg2


def create_connection():
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="user_postgres",
            password="pass_postgres",
            host="localhost",
            port="5432",
        )
        return connection
    except Exception as e:
        print(f"La connexió ha fallat: {e}")
        return None
