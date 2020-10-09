from mysql.connector import pooling
from mysql import connector
import logging


class BaseMySQL(object):

    def __init__(self, host="127.0.0.1", port=3306, user="root", password=None, database=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        res = dict()
        res["host"] = self.host
        res["port"] = self.port
        res["user"] = self.user
        res["password"] = self.password
        res["database"] = self.database
        self.dbconfig = res
        self.pool = self.create_pool()

    def create_pool(self, pool_name="mypool", pool_size=3):
        """
        Create a connection pool, after created, the request of connecting
        MySQL could get a connection from this pool instead of request to
        create a connection.
        :param pool_name: the name of pool, default is "mypool"
        :param pool_size: the size of pool, default is 3
        :return: connection pool
        """
        pool = pooling.MySQLConnectionPool(
            ssl_disabled=True,
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **self.dbconfig)
        return pool

    def close(self, conn, cursor):
        """
        A method used to close connection of mysql.
        :param conn:
        :param cursor:
        :return:
        """
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    def connect(self):
        connection = connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return connection

    def insert_update(self, query, values):
        try:
            connection = self.pool.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()

        except connector.Error as error:
            # self.logger.error("Failed to insert into MySQL table {0}".format(error))
            return error
        finally:
            self.close(connection, cursor)
            # self.logger.debug("MySQL Connection Closed.")

    def execute_query(self, query, values):
        try:
            connection = self.pool.get_connection()
            cursor = connection.cursor()
            cursor.execute(query, values)
            records = cursor.fetchall()
            return records
        except connector.Error as error:
            # self.logger.error("Failed to insert into MySQL table {0}".format(error))
            return error

        finally:
            self.close(connection, cursor)
            # self.logger.debug("MySQL Connection Closed.")
