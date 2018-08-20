import sqliteModel
import RelationshipModel
import CommonClass
import datetime


class RelationshipController(RelationshipModel.Friend):
    common = CommonClass.Common()
    sql = sqliteModel.Sqlite()

    def __init__(self, user1=0, user2=0, period='', _isblock=0):
        super().__init__(user1, user2, period, _isblock)

    def checkIsFriend(self, id, userId):

        query = "select DISTINCT friend_list.id, friend_list.user1, friend_list.user2 from users, friend_list where (user1= "+str(
            userId)+" and users.id=  "+str(userId)+" ) or (user2= "+str(userId)+"  and users.id=  "+str(userId)+") and friend_list.blocked=0 ;"
        frList = self.sql.executeSelect(query)
        isFriend = False
        for fr in frList:
            if (fr[1] == id and fr[2] == userId) or (fr[1] == userId and fr[2] == id):
                print('you re friend!')
                isFriend = True
                return isFriend
        return isFriend

    def addNewFriend(self, userId, id):
        query = "insert into friend_list(user1, user2, period) values("+str(userId)+","+str(id)+",'"+str(datetime.datetime.now())+"');"
        self.sql.execute(query)

    def displayMyFriendlist(self, userId):
        query = "select DISTINCT friend_list.user1, friend_list.user2 from users, friend_list where (user1= "+str(
            userId)+" and users.id=  "+str(userId)+" ) or (user2= "+str(userId)+"  and users.id=  "+str(userId)+") and friend_list.blocked=0 ;"
        frList = self.sql.executeSelect(query)
        return frList

    def blockUser(self, username):
        query= "UPDATE friend_list SET blocked=0 WHERE user1= (SELECT users.id FROM users WHERE users.username= '{}') or user2= (SELECT users.id FROM users WHERE users.username='{}')".format(username,username)
        self.sql.execute(query)

    def getFriendUserName(self, user2):
        query= "SELECT DISTINCT users.username from users, friend_list WHERE users.id= friend_list.user2 AND friend_list.user2= {}".format(user2)
        friendUsername= self.sql.executeSelect(query)
        return friendUsername[0][0]

