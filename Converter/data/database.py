from mariadb import connect

USER='root'
PASSWORD='76543210'
HOST='localhost'
PORT=3306
DATABASE='ko_converter_db'

def _get_connection():
    return connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=3306,
        database=DATABASE
    )


def read_query(sql: str, sql_params=()):
    with _get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, sql_params)

        return list(cursor)


def insert_query(sql: str, sql_params=()) -> int:
    with _get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, sql_params)
        conn.commit()

        return cursor.lastrowid


def update_query(sql: str, sql_params=()) -> bool:
    with _get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, sql_params)
        conn.commit()

        return cursor.rowcount