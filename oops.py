# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# prashant = Employee("Prashant", "43430000000")
# print(prashant.name)
# print(prashant.salary)
#
# someoneElse = Employee("IDK the name", "12000")
# print(someoneElse.name)
# print(someoneElse.salary)

class Parrot:

    #name and age are the attributes/properties of the Parrot
    name = ""
    age = 0

# Creating an object of Parrot Class

parrot1 = Parrot() # parrot1 is an object for class Parrot
parrot1.name = "Hero"
parrot1.age = "13"

# Creating another object of Parrot Class

parrot2 = Parrot()
parrot2.name = "Dosro"
parrot2.age = "4"

#Accessing the attributes/properties

print(f"{parrot1.name} is {parrot1.age} years old.")
print(f"{parrot2.name} is {parrot2.age} years old.")

# Inheritance in OOPS

class Bird: #Base Class

    def eat(self):
        print("I can eat")
    def fly(self):
        print("I can fly")

class hummingBird(Bird): # Derived Class

    def flyBackwards(self):
        print("I can fly Backwards")

hummingBird1 = hummingBird()
hummingBird1.fly()
hummingBird1.flyBackwards()

# Encapsulation

class Mobile:
    def __init__(self):
        self.__maxprice = 15000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

mob = Mobile()
mob.sell()

# Changing the price directly - no effect

mob.__maxprice = 20000
mob.sell()

# using the setMaxPrince Function
mob.setMaxPrice(25000)
mob.sell()

# Polymorphism - Same entity different operations

class Polygon:
    def render(self):
        print("Rendering a polygon")
class Square(Polygon):
    def render(self):
        print("Rendering a Square")
class Circle:
    def render(self):
        print("Rendering a Circle")

p1 = Polygon()
p1.render()

c1 = Circle()
c1.render()










