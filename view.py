import usersController
import messageController
import switchClass
import RelationshipController
import datetime
import CommonClass


class View():

    def __init__(self):
        self.uc = usersController.usersController(0, '', '', '', '', '')
        self.msgc = messageController.MessageController('', 0, 0, '', 0)
        self.rc = RelationshipController.RelationshipController(0, 0, '', 0)
        self.com = CommonClass.Common()
        self.sw = switchClass.switcher()

    def signUp(self):
        username = input('Input your Username: ')
        if self.com.checkSpace(username) == False:
            id = self.com.CheckUser(username)
            if id != None:
                print('this Username has taken by another! Try another username!')
                return 0
            else:
                while 1:
                    password = input('Type your password here: ')
                    tempPassword = input('Type your password again: ')
                    if tempPassword != password:
                        continue
                    else:
                        fullname = input('Type your fullname: ')
                        address = input('Type your address: ')
                        Email = input('Type your email: ')
                        self.uc.SignUp(username, password,
                                       fullname, address, Email)
                        continue
        else:
            print('Username doesnt not have space!')

    def singIn(self):
        username = input('Enter your user name: ')
        if(self.com.checkSpace(username) == False) and self.com.CheckUser(username) != None:
            password = input('Enter your password: ')
            self.uc.signIn(username, password)
            return self
        else:
            print('or your password is not right! please try again!')

    def modifyUserInformation(self):
        sw = switchClass.switcher()
        choose = input(
            'Choose 1-4 to modify your information: \n1: Modify your password\n2: Modify your fullname\n3: Modify your address\n4: Modify your Email\nYour choose: ')
        if choose == '1':
            # newName = input('Enter your correct name: ')
            oldPassword = input('Enter your current password: ')
            PasswordOfUser = self.uc.getPassword()
            if oldPassword == PasswordOfUser:
                newPassword = input('Enter your new password: ')
                temp = input('Enter it again: ')
                if temp == newPassword:
                    self.sw.modifypassword(
                        self.uc.id, oldPassword, newPassword)
                else:
                    print("the pair password must be matched!")
            else:
                print('your password is not right! please try again!')
        if choose == '2':
            newName = input('Type your new name: ')
            self.sw.modifyFullname(self.uc.id, newName)
        if choose == '3':
            newAddress = input('Enter your new address: ')
            self.sw.modifyAddress(self.uc.id, newAddress)
        if choose == '4':
            newEmail = input('Enter your new email: ')
            sw.modifyEmail(self.uc.id, newEmail)
        else:
            return None

    def disPlayAllMyMsgs(self):
        self.msgc.displayAllMyMsg(self.uc.id)

    def sendMsg(self):
        username = input('Type username you wanna chat: ')
        if self.com.checkSpace(username) == False:
            id = self.com.CheckUser(username)
            if id != 0:
                content = input('Type something to your friend: ')
                self.msgc.sendMsg(self.uc.id, id, content)

    def addNewFriend(self):
        username = input('Input username to add your friend list: ')
        if self.com.checkSpace(username) == False:
            id = self.com.CheckUser(username)
            if id != None:
                isfriend = self.rc.checkIsFriend(id, self.uc.id)
                if isfriend == False:
                    self.rc.addNewFriend(self.uc.id, id)
                    print('added {} to your friendlist!'.format(username))

    def displayMyFriendList(self):
        self.rc.displayMyFriendlist(self.uc.id)

    def blockUser(self):
        username = input('type username you want to block: ')
        if self.com.checkSpace(username) == False:
            self.rc.blockUser(username)
            print('Success!')

    def displayNotBeSeenMsgs(self):
        notBeSeenMsgsList = self.msgc.displayNotBeSeenMsgs(self.uc.id)
        for msg in notBeSeenMsgsList:
            print(msg)


def main():
    a = View()
    while 1:
        print('1: Sign up\n2: Sign In\n')
        choose1 = input('Choose 1 or 2 to continue: ')
        if choose1 == '1':
            a.signUp()
            continue
        if choose1 == '2':
            a.singIn()
            while 1:
                print('1: Display all my messages')
                print('2: Display all my messages have not been read')
                print('3: Send message')
                print('4: Display my friendlist')
                print('5: Add new friend')
                print('6: Block ')
                print('7: Modify my information')
                print('8: Log out')
                choose2 = input('Choose 1-7 to continue: ')
                if choose2 == '1':
                    a.disPlayAllMyMsgs()
                    continue
                if choose2 == '2':
                    a.displayNotBeSeenMsgs()
                    continue
                if choose2 == '3':
                    a.sendMsg()
                    continue
                if choose2 == '4':
                    a.displayMyFriendList()
                    continue
                if choose2 == '5':
                    a.addNewFriend()
                    continue
                if choose2 == '6':
                    a.blockUser()
                    continue
                if choose2 == '7':
                    a.modifyUserInformation()
                    continue
                if choose2 == '8':
                    return 0
            continue


if __name__ == '__main__':
    main()
