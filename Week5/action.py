                    #ACTIVITY 2
class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Driving on the road")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")


class Ship(Vehicle):
    def move(self):
        print("sailing in the sea")


Vehicles = [Car(), Plane(), Ship()]


for v in Vehicles:
    v.move()
   
   

