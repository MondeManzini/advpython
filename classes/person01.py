from decorators.decorate_class import debugclass
@debugclass
class Person(object):
    
    def __init__(self,name='', age=0):
        self.name = name
        self.age = age

    def talk(self):
        return "my name is %s" % self.name

    def walk(self):
        if self.age <= 1: return "crawl"
        elif self.age<75: return "walk"
        else : return "hobble"
    
    @staticmethod
    def test_person(pers):
        print(pers.talk())
        print(pers.walk())

if __name__ == '__main__':
    fred = Person('Fred',10)
    Person.test_person(fred)
    Person.test_person(Person('sally',80))
