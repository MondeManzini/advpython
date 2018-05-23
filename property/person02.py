class Person(object):

    def __init__(self,name, age=0):
        self.set_name(name)
        self.age = age

    def get_name(self):
        return self.fname + ' ' + self.surname

    def set_name(self,name):
        if ' ' in name:
            self.fname,self.surname = name.split(' ')
        else:
            self.fname = name
            self.surname = ''

    name = property(get_name, set_name)

def test_person(pers):
    print 'Name:',pers.name, 'Age:',pers.age

if __name__ == '__main__':
    fred = Person('Fred',10)
    test_person(fred)
    test_person(Person('Sally Derkins',80))
    print fred.fname
