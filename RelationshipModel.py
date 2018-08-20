class Friend(object):
    def __init__(self,user1=0 , user2= 0, period= 0, _isblock= 0):
        self.user1= user1
        self.user2= user2
        self.period= period
        self._isblock= _isblock
    
    def getStatus(self):
        return self._isblock
        
        