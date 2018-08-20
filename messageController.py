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
        query = "SELECT message.receiver, message.sender, message.status, message.time FROM message, users WHERE (users.id= message.sender AND users.id= "+str(
            id)+") OR (users.id= message.receiver AND users.id="+str(id)+") order by message.id desc;"
        msgs = self.sql.executeSelect(query)
        for msg in msgs:
            self.lisMsgs.append(msg)
            print('\n', msg)

    def sendMsg(self, userId, id, content):
        query = "INSERT into message(sender, receiver, contents, time) values("+str(userId)+","+str(id) + ",'"+content+"','"+time.ctime()+"');"
        self.sql.execute(query)
        print('Send message successfully!')
