class Message(object):
    def __init__(self, _content='', _sender=0, _receiver=0, _time='', _status=0):
        self._content = _content
        self._sender = _sender
        self._receiver = _receiver
        self._time = _time
        self._status = _status

    def getContent(self):
        return self._content

    def getSender(self):
        return self._sender

    def getReceiver(self):
        return self._receiver

    def getTime(self):
        return self._time

    def getStatus(self):
        return self._status
