import sqliteModel


class switcher(object):
    def __init__(self):
        self.sql = sqliteModel.Sqlite()
    def modifyFullname(self, userId, newName):
        query = "update users set fullname= '{}' where users.id= {};".format(
            newName, userId)
        self.sql.execute(query)
        print("Modify Fullname success!")

    def modifyAddress(self, id, newAddress):
        query = "update users set address= '{}' where users.id= {};".format(
            newAddress, id)
        self.sql.execute(query)
        print("Modify Address success!")

    def modifyEmail(self, id, newEmail):
        query = "update users set Emails= '{}' where users.id= {};".format(newEmail, id)
        self.sql.execute(query)
        print("Modify nAddress success!")

    def modifypassword(self,userId, oldPassword, newPassword):
        query = "update users set passwords= '{}' where users.id= {};".format(newPassword, userId)
        self.sql.execute(query)
        print('Change success!')


