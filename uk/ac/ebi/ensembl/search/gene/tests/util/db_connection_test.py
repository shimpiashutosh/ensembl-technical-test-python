import sqlite3


class DBConnectionTest:

    def __init__(self):
        self.conn = sqlite3.connect(":memory:")

    def fetch_db_result(self, sql):
        cursor = self.conn.cursor()
        return cursor.execute(sql).fetchall()

    def __del__(self):
        self.conn.close()
