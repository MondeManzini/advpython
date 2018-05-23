class Person(object):

    def __init__(self,_name, age=0):
        self.name = _name
        self.age = age

    @property
    def name(self):
        return self.fname + ' ' + self.surname

    @name.setter
    def name(self,_name):
        if ' ' in _name:
            self.fname,self.surname = _name.split(' ')
        else:
            self.fname = _name
            self.surname = ''

def test_person(pers):
    print 'Name:',pers.name, 'Age:',pers.age

if __name__ == '__main__':
    fred = Person('Fred',10)
    test_person(fred)
    test_person(Person('Sally Derkins',80))
    print fred.fname
