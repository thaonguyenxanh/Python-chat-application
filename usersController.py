import sqlite3
import switchClass
import sqliteModel
import UserModel
import CommonClass


class usersController(UserModel.users):

    def __init__(self, id=0, username='', _password='', fullname='', _address='', _email=''):
        self.sql = sqliteModel.Sqlite()
        self.common = CommonClass.Common()
        super().__init__(id, username, _password, fullname, _address, _email)

    def SignUp(self, username, password, fullname, address, Email):
        query = "insert into users(username,passwords,fullname,address,Emails) values('{}','{}','{}','{}','{}')".format(
            username, password, fullname, address, Email)
        self.sql.execute(query)
        print('Success!, welcome to our mini chat application!')

    def signIn(self, username, password):
        query = "select * from users where users.username= '{}' and users.passwords= '{}'".format(
            username, password)
        user = self.sql.executeSelect(query)
        if user != None:
            for row in user:
                id = int(row[0])
                if id != 0:
                    self.id = row[0]
                    self.username = row[1]
                    self._password = row[2]
                    self.fullname = row[3]
                    self._address = row[4]
                    self._email = row[5]
                    print('Success!')
                    return self
        else:
            print('your password is not right! please try again!')
