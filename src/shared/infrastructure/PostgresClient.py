from functools import wraps

from psycopg2.extras import RealDictCursor


class PostgresClient:

    def __init__(self,
                 host: str,
                 port: int,
                 user: str,
                 password: str,
                 db_name: str):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__db_name = db_name

    @staticmethod
    def create_client(
            host: str,
            port: int,
            user: str,
            password: str,
            db_name: str
    ):
        return PostgresClient(host, port, user, password, db_name)

    def __connect(f):
        @wraps(f)
        def wrapper(self, *args, **kwargs):
            import psycopg2
            cursor = None
            conn = None
            result = None
            try:
                conn = psycopg2.connect(
                    host=self.__host,
                    port=self.__port,
                    dbname=self.__db_name,
                    user=self.__user,
                    password=self.__password,

                )
                cursor = conn.cursor(cursor_factory=RealDictCursor)
                result = f(self, cursor, *args, **kwargs)
            except Exception as e:
                print(e)
                if cursor is not None:
                    cursor.close()
                if conn is not None:
                    conn.close()
                raise Exception("Error trying to connect with database")
            finally:
                if cursor is not None:
                    cursor.close()
                if conn is not None:
                    conn.close()
                return result
        return wrapper

    @__connect
    def execute_query(self, cursor, query: str, params: dict):
        cursor.execute(query, params)
        response = cursor.fetchall()
        return list(response)

    @__connect
    def execute_aggregated_query(self, cursor, query: str, params: dict):

        cursor.execute(query, params)
        response = cursor.fetchone()
        return dict(response or {}) or None
