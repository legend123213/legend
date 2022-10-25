class Give():
    username = None
    def __init__(self,username):
        self.username = username
    def ret(self):
        return self.username
class Take(Give):
    def on(self):
        Give('kok')
        print(Give.ret(self))
o = Take('koooo')
o.on()