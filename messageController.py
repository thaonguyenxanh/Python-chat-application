import MessageModel
import CommonClass
import sqliteModel
import time


class MessageController(MessageModel.Message):
    common = CommonClass.Common()
    sql = sqliteModel.Sqlite()
    lisMsgs = []

    def __init__(self, _content='', _sender=0, _receiver=0, _time='', _status=0):
        super().__init__(_content, _sender, _receiver, _time, _status)

    def displayAllMyMsg(self, id):
        query = "SELECT message.receiver, message.sender, message.time FROM message, users WHERE (users.id= message.sender AND users.id= "+str(
            id)+") OR (users.id= message.receiver AND users.id="+str(id)+") order by message.id desc;"
        msgs = self.sql.executeSelect(query)
        return msgs

    def sendMsg(self, userId, id, content):
        query = "INSERT into message(sender, receiver, contents, time) values("+str(
            userId)+","+str(id) + ",'"+content+"','"+time.ctime()+"');"
        self.sql.execute(query)
        print('Send message successfully!')

    def displayNotBeSeenMsgs(self, userId):
        query = "select message.id,message.contents, message.sender from message, users where users.id= {} and message.receiver=users.id and message.status=0 order by message.id desc".format(
            userId)
        NotBeSeenMsgsList = self.sql.executeSelect(query)
        return NotBeSeenMsgsList

    def getUserName(self, user2):
        query = "SELECT DISTINCT users.username from users, message WHERE users.id= message.sender and message.sender= {}".format(
            user2)
        user = self.sql.executeSelect(query)
        return user

    def getUsername2(self, id):
        query = "select distinct users.username from users where users.id={}".format(
            id)
        return self.sql.executeSelect(query)
