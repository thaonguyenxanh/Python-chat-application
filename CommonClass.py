import sqliteModel
import sqlite3


class Common:
    sql = sqliteModel.Sqlite()

    def checkSpace(self, username):
        hasSpace= False
        for index in range(len(username)):
            if username[index] == ' ':
                hasSpace= True
                print('username doesnot have space!')
                return hasSpace
        return hasSpace


    def CheckUser(self, username):
        id = 0
        query1 = "select * from users where users.username= '{}';".format(
            username)
        try:
            user = self.sql.executeSelect(query1)

            for row in user:
                if row[1] == username:
                    id = int(row[0])
                    return id
                else:
                    return 0
        except sqlite3.Error as e:
            print('an Error occurred: ', e.args[0])
