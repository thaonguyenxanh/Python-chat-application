class users(object):
    def __init__(self,id= 0, username='', _password='', fullname='', _address='', _email=''):
        self.username = username
        self._password = _password
        self.fullname = fullname
        self._address = _address
        self._email = _email
        self.id= id

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self._password

    def getFullname(self):
        return self.fullname

    def getAddress(self):
        return self._address

    def getEmail(self):
        return self._email
