class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        print 'getting x'
        return self._x
    def setx(self, value):
        print 'setting x'
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")
