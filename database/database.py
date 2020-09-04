from authentication.database_auth import DB_NAME, USER, PASSWORD, HOST, PORT
import psycopg2


class Database(object):
    _conn = None

    def get_connection(self):
        if self._conn is None:
            try:
                self._conn = psycopg2.connect("dbname={} user={} password={} host={} port={}".format(
                    DB_NAME, USER, PASSWORD, HOST, PORT
                ))
            except psycopg2.Error:
                print('Error - failed to connect to database')
        print('Successfully connected to database')
        return self._conn

    def get_connection_decorator(self):
        return

    def close_connection(self):
        if self._conn is not None and self._conn.closed > 0:
            self._conn.close()
        self._conn = None
        print('Successfully closed connection')

