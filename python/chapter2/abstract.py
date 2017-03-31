from abc import ABCMeta, abstractmethod

class Headers(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.headers = ' '

    @abstractmethod
    def _getBaiduHeaders(self):
        pass

    def __str__(self):
        return self.headers

class BaiduHeaders(Headers):

    def _getBaiduHeaders(self, username):
        self.headers = username


b = BaiduHeaders()
b._getBaiduHeaders("A")
print b

