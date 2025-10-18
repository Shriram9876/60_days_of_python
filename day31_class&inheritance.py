#exercise 1
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"die buch ist raufst {self.title} und ist schreibt by {self.author} ein")

buch = Book("Faun", "jane")
buch.display_info()

#exercise 2
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, fuel_type):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

auto = Car("Porsche", "2024", "petrol")
print(auto.brand)
print(auto.year)
print(auto.fuel_type)

#exercise 3
class Teacher:
    def __init__(self, Teach):
        self.Teach = Teach
    
    def Teaching(self):
        return "teaching the students statistics"

class Student:
    def __init__(self, student):
        self.student = student
    
    def student1(self):
        return "studying statistics"

class Teaching_Assistant(Teacher, Student):
    def __init__(self, Teach, student):
        Teacher.__init__(self, Teach)
        Student.__init__(self, student)

# Create an instance with both required arguments
mortiz = Teaching_Assistant("Dr. Smith", "Mortiz")

# Call methods
print(mortiz.student1())
print(mortiz.Teaching())

#exercise 4
class animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return "the animal  sound will be written here"

class Hund(animal):
    def speak(self):
        return f"{self.name} der hund barks"

class katze(animal):
    def speak(self):
        return f"{self.name} die katze meows"

hund1 = Hund("Moritz")
print(hund1.speak())

katze1 = katze("Dan")
print(katze1.speak())