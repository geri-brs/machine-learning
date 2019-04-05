#Define Car class
class Car:
    def __init__(self, name, color, condition, age):
        self.name = name
        self.color = color
        self.condition = condition
        self.age = age
    
    def description(self):
        print(self.name + " " + self.color + " " +
              self.condition + " " + self.age)
    
#Create an object
cars = list()
cars.append(Car("Audi", "green", "good", "2015"))
cars.append(Car("Volvo", "grey", "amazing", "2011"))
cars.append(Car("Maserati", "black", "bad", "2018"))
cars.append(Car("Toyota", "red", "good", "2008"))

import operator
cars.sort(key=operator.attrgetter('age'))
for car in cars:
    print (car.name + " " + car.color + " " + car.condition + " " + car.age)


