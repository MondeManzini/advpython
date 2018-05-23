import decorate_class as dc
@dc.debugclass
class Person(object):
    
    def __init__(self,name='', age=0):
        self.name = name
        self.age = age
    def getname(self): return self.name
    def getage(self): return self.age

def test_person(pers):
    print 'Name:',pers.getname(), 'Age:',pers.getage()

if __name__ == '__main__':
    fred = Person('Fred',10)
    test_person(fred)
    test_person(Person('sally',80))
