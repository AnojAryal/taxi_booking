# import psycopg2

# class Database_connection:


#     hostname = 'localhost'
#     database = 'taxi_dbms'
#     username = 'anoj'
#     pwd = 'fastrack'
#     port_id = 5432


#     def connection(self):
#         try:
#             connection_db = psycopg2.connect(
#                 host=self.hostname,
#                 dbname=self.database,
#                 user=self.username,
#                 password=self.pwd,
#                 port=self.port_id
#             )
#             return connection_db

#         except Exception as error:
#             print(error)

import psycopg2


class SysDb:
    message = ""

    @staticmethod
    def Connection():
        try:
            conn = psycopg2.connect(
                host="localhost",
                dbname="ridex_dbms",
                user="franzy",
                password="anoj",
                port=5432,
            )
            return conn

        except Exception as error:
            SysDb.message = error
