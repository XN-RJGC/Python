# connect_mongodb.py
"""
a simaple class to connect mongodb
"""
import pymongo

class connect_mongodb:
    """
    a class to connect mongodb database.
    """
    def __init__(self, host='localhost', port=27017):
        """
        Using host of string and port of int to connect mongodb database.
        :param host: string
        :param port:  int
        """
        self.host = host
        self.port = port

    # get connect
    def get_connect(self):
        """
        Connect mongodb database.
        :return: if connect error return None else return connection object
        """
        connection = pymongo.MongoClient(self.host, self.port)
        if connection is not None:
            return connection
        else:
            return None