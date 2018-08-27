import usersController
import messageController
import switchClass
import RelationshipController
import datetime
import CommonClass
from msvcrt import getch


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
                        break
        else:
            print('Username doesnt not have space!')

    def singIn(self):
        username = input('Enter your user name: ')
        if(self.com.checkSpace(username) == False) and (self.com.CheckUser(username) != None):
            password = input('Enter your password: ')
            if(self.uc.signIn(username, password)!= None):
                return self
        else:
            print('or your password is not right! please try again!')
            return None
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
        msgs = self.msgc.displayAllMyMsg(self.uc.id)
        for msg in msgs:
            tempList = []
            for inf in msg:
                tempList.append(inf)
            for i in range(1,3):
                if tempList[i] == self.uc.id:
                    tempList[i] = self.msgc.getUsername2(self.uc.id)[0][0]
                else:
                    tempList[i] = self.msgc.getUsername2(tempList[i])[0][0]
            print(tempList)

    def sendMsg(self):
        username = input('Type username you wanna chat: ')
        if self.com.checkSpace(username) == False:
            id = self.com.CheckUser(username)
            if id != 0:
                content = input('Type something to your friend: ')
                self.msgc.sendMsg(self.uc.id, id, content)
    def sendMsg2(self, id):
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
        frList = self.rc.displayMyFriendlist(self.uc.id)
        tempList=[]
        for fr in frList:
            tempList1 = []
            for inf in fr:
                tempList1.append(inf)
            tempList.append(tempList1)
            for i in range(1,3):
                if tempList1[i] != self.uc.id:
                    tempList1[i] = self.rc.getFriendUserName(tempList1[i])
                else:
                    tempList1[i] = self.rc.getFriendUserName(self.uc.id)
        for tl in tempList:
            print(tl)
        return frList

    def blockUser(self):
        username = input('type username you want to block: ')
        if self.com.checkSpace(username) == False:
            self.rc.blockUser(username)
            print('Success!')

    def displayNotBeSeenMsgs(self):
        notBeSeenMsgsList = self.msgc.displayNotBeSeenMsgs(self.uc.id)
        for msg in notBeSeenMsgsList:
            listTemp = []
            for i in msg:
                listTemp.append(i)
            listTemp[2] = self.msgc.getUserName(listTemp[2])[0][0]
            print(listTemp)
    def displayFriendListOrderByAddress(self):
        self.rc.displayFriendListOrderByAdress(self.uc.id)

def main():
    a = View()
    while 1:
        print('1: Sign up\n2: Sign In\n')
        choose1 = input('Choose 1 or 2 to continue: ')
        if choose1 == '1':
            while 1:
                a.signUp()
                break
        if choose1 == '2':
            signIn= a.singIn()
            if signIn != None:
                while 1:
                    print('1: Display all my messages')
                    print('2: Display all my messages have not been read')
                    print('3: Send message')
                    print('4: Display my friendlist')
                    print('5: Add new friend')
                    print('6: Block ')
                    print('7: Modify my information')
                    print('8: Display friendlist order by address')
                    print('9: Log out')
                    # choose2 = input('Choose 1-9 to continue: ')
                    print('Choose 1-9 to continue: ')
                    print('Press Ctrl-L to back to display friendlist: ')
                    print('Press Ctrl-B to back to previous menu, press anything else to continue: ')
                    choose2= ord(getch())
                    print('\n\n\n')
                    if choose2== 2:
                            break
                    if choose2== 12:
                        print('Press Ctrl-B to back to previous menu, press anything else to continue: ')
                        choose= ord(getch())
                        if choose== 2:
                            break
                        else:    
                            frList= a.displayMyFriendList()
                            print(frList)   
                            print('Press from {} to {} matching relationship id to send a new message: '.format(frList[0][0], frList[len(frList)-1][0]))
                            i= int(input())
                            for fr in frList:
                                if i== fr[0]:
                                    for index in fr:
                                        if int(index) != a.uc.id:
                                            a.sendMsg2(int(index))
                                            continue
                            continue
                            
                    if choose2== 2:
                        break
                    if choose2 == 49:
                        print('Press Ctrl-B to back to previous menu, press anything else to continue: ')
                        choose= ord(getch())
                        if choose== 2:
                            break
                        else:
                            a.disPlayAllMyMsgs()
                            continue
                    if choose2 == 50:
                        print('Press Ctrl-B to back to previous menu, press anything else to continue: ')
                        choose= ord(getch())
                        if choose== 2:
                            break
                        else:                    
                            a.displayNotBeSeenMsgs()
                            continue
                    if choose2 == 51:
                        print('Press Ctrl-B to back to previous menu, press anything else to continue: ')
                        choose= ord(getch())
                        if choose== 2:
                            break
                        else:
                            a.sendMsg()
                            continue
                    if choose2 == 52:
                        print('Press Ctrl-B to back to previous menu, press anything else to continue: ')
                        choose= ord(getch())
                        if choose== 2:
                            break
                        else:
                            a.displayMyFriendList()
                            continue
                    if choose2 == 53:
                        print('Press Ctrl-B to back to previous menu, press anything else to continue: ')
                        choose= ord(getch())
                        if choose== 2:
                            break
                        else:                    
                            a.addNewFriend()
                            continue
                    if choose2 == 54:
                        print('Press Ctrl-B to back to previous menu, press anything else to continue: ')
                        choose= ord(getch())
                        if choose== 2:
                            break
                        else:                
                            a.blockUser()
                            continue
                    if choose2 == 55:
                        print('Press Ctrl-B to back to previous menu, press anything else to continue: ')
                        choose= ord(getch())
                        if choose== 2:
                            break
                        else:
                            a.modifyUserInformation()
                            continue
                    if choose2 == 56:
                        print('Press Ctrl-B to back to previous menu, press anything else to continue: ')
                        choose= ord(getch())
                        if choose== 2:
                            break
                        else:                    
                            a.displayFriendListOrderByAddress()
                            continue
                    if choose2 ==57:
                        break
                continue
                


if __name__ == '__main__':
    main()
