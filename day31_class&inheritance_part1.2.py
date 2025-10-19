#exercise 1
class Car:
    wheels = 4

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

car1 = Car("Ford","mustang")
car2 = Car("vaxhaul", "corsa")

print(car1.wheels)
print(car2.wheels)

Car.wheels = "Ferrari","FXX-k Evo"
print(Car.wheels)

print(car1.brand)
print(car2.model)

#exercise 2
class Person:
    def __init__(self,name):
        self.name = name
    
    def intro(self):
        print(f"hallo, mein name ist {self.name}")

class Student(Person):
    def intro(self):
        super().intro()
        print(f"ich heise {self.name}")

leute = Student("karl")
leute.intro()

#exercise 3
class A:
    def process(self):
        print("a")

class B(A):
    def process(self):
        print("b")
        super().process()

class C(B):
    def process(self):
        print("c")
        super().process()

class D(B,C):
    def process(self):
        print("d")
        super().process()

D.process()

class A:
    def process(self):
        print("a")

class B(A):
    def process(self):
        print("b")

class C(B):
    def process(self):
        print("c")

class D(B, C):
    def process(self):
        print("d")
        super().process()

obj = D()
obj.process()

#exercise 4
class Address:
    def __init__(self, stadt, country):
        self.stadt = stadt
        self.country = country

    def display_info(self):
        print(f"mein adresse ist {self.stadt} und ich bin aus {self.country}")

class Person:
    def __init__(self, stadt, country):
        self.address = Address(stadt, country)

    def info(self):
        self.address.display_info()
        print("hallo und willkommen")

# Create a Person with address details
person1 = Person("München", "Deutschland")
person1.info()