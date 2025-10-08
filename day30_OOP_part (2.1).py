#exercise 1
class hund:
    def speak(self):
        return "woof!"

class katze:
    def speak(self):
        return "meow!"

for animal in [hund(), katze()]:
    print(animal.speak())

#exercise 2 (the wrong version)
class car:
    def move(self):
        return "it goes on land"

class boat:
    def move(self):
        return "it goes on water"

for vehicle in [car(), boat()]:
    class start_journey(vehicle):
            print(vehicle.move)

class Car:
    def move(self):
        return "It goes on land"

class Boat:
    def move(self):
        return "It goes on water"

class JourneyStarter:
    def start_journey(self, vehicle):
        # Duck typing: we assume vehicle has a move() method
        print(vehicle.move())

# Example usage
vehicles = [Car(), Boat()]
starter = JourneyStarter()

for v in vehicles:
    starter.start_journey(v)

#exercise 3
class Employee:
    def work(self):
        return "was ist dein beruf?"
    
class Developer(Employee):
    def work(self):
        return "bist du ein Developer?"
    
class Designer(Employee):
    def work(self):
        return "bist du ein Designer?"

for arbeit in [Employee(), Developer(), Designer()]:
    print(arbeit.work())

#exercise 4
from abc import ABC, abstractmethod

class Appliance(ABC):
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class Light(Appliance):
    def turn_on(self):
        return "turning on the lights"
    
    def turn_off(self):
        return "turning off the lights"

class Fan(Appliance):
    def turn_on(self):
        return "turning on the fan"
    
    def turn_off(self):
        return "turning off the fan"

appliance = Fan()
appliance2 = Light()
print(appliance2.turn_on(), appliance.turn_off())

#exercise 5
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# Example usage
circle = Circle(5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

rectangle = Rectangle(4, 5)
print("Rectangle Perimeter:", rectangle.perimeter())

rectangle2 = Rectangle(6, 8)
print("Rectangle Area:", rectangle2.area())

#exercise 6
from abc import ABC, abstractmethod

# Abstract base class
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete class for Credit Card payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

# Concrete class for UPI payment
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

# Concrete class for PayPal payment
class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")