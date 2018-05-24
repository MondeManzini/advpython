class Car(object):
    def __init__(self):
       self.speed = 0

    def accel(self, amount):
        self.speed += amount
    def brake(self, amount):
        self.speed -=amount


ferrari = Car()
ferrari.accel(5)
Car.accel(ferrari, 5)
print ferrari.speed
