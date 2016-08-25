# connect_mysql.py
"""
connect mysql database.
"""
import mysql.connector

# database name
class connect_mysql:
    """
    connect mysql database.
    """
    def __init__(self, host, port, database_name, user_name, password):
        self.database_name = database_name
        self.host = host
        self.port = port
        self.user_name = user_name
        self.password = password

    # connect
    @property
    def get_connect(self):
        try:
            connect = mysql.connector.connect(host=self.host, port=self.port,
                                              user=self.user_name, password=self.password,
                                              database=self.database_name)
            return connect
        except mysql.connector.Error:
            return None

    # get cursor
    @staticmethod
    def get_cursor(connect):
        if connect is not None:
            return connect.cursor()
        else:
            return None

    # close cursor
    @staticmethod
    def cursor_close(self, cursor):
        if cursor is not None:
            cursor.close()

    # close
    @staticmethod
    def connect_close(self, connect):
        if connect is not None:
            connect.close()

    # close all
    @staticmethod
    def close_all(self, cursor, connect):
        if cursor is not None:
            cursor.close()
        if connect is not None:
            connect.close()