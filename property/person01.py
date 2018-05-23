class Person(object):
    
    def __init__(self,name='', age=0):
        self.name = name
        self.age = age

def test_person(pers):
    print 'Name:',pers.name, 'Age:',pers.age

if __name__ == '__main__':
    fred = Person('Fred',10)
    test_person(fred)
    test_person(Person('sally',80))
