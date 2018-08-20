import sqlite3


class Sqlite:
    def connectDb(self):
        try:
            self.conn = sqlite3.connect("chatapp.db")
            self.cur = self.conn.cursor()
            # print('connected database!')
            return self.cur
        except sqlite3.Error as e:
            print('An error occurred: ', e)

    def closeDb(self):
        self.conn.commit()
        self.conn.close()

    def execute(self, query):
        try:
            self.connectDb()
            self.cur.execute(query)
            self.closeDb()
            return self.cur
        except sqlite3.Error as e:
            print('An error occurred: ', e)

    def executeSelect(self, query):
        try:
            self.connectDb()
            self.cur.execute(query)
            self.list = self.cur.fetchall()
            self.closeDb()
            return self.list
        except sqlite3.Error as e:
            print('An error occurred: ', e)

    def getError(self):
        return sqlite3.Error()
