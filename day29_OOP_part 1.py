#exercise 1
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def my_car(self):
        print(f"my car is from {self.brand} is a {self.model}")

car1 = car("BMW", "M3 GTR")
car2 = car("mclaren", "F1")

car1.my_car()
car2.my_car()

#exercise 2
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def about_person(self):
        print(f"the person's name is {self.name} and age is {self.age}")

leut = person("eddy",23)

leut.about_person()

#exercise 3
class book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    
    def about_book(self):
        print(f"the book's title is {self.title}, followed by author's name {self.author} and last but least from which year {self.year}")

book1 = book("phhp","kein ahnung", 2022)
book2 = book("tbate","turtleme",2018)
book3 = book("solo leveling","jin hyuuk", 2018)

book1.about_book()
book3.about_book()
book2.about_book()

#exercise 4
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited successfully. Current balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Money withdrawn successfully. Remaining balance: {self.balance}")

# Input and usage
amount = int(input("Enter the amount to deposit/withdraw: "))
owner1 = BankAccount("Moritz", 150000)

owner1.deposit(amount)
owner1.withdraw(amount)

#i noticed that i wasn't able to do different operations so i just asked AI to reconfigure that way anyway i will leave my original code to be pointed out what i did wrong
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount} successfully. Current balance: ₹{self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount} successfully. Remaining balance: ₹{self.balance}")

# Create account
owner1 = BankAccount("Moritz", 150000)

# Ask user for action
action = input("Do you want to deposit or withdraw? ").strip().lower()

if action in ["deposit", "withdraw"]:
    try:
        amount = int(input(f"Enter the amount to {action}: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif action == "deposit":
            owner1.deposit(amount)
        else:
            owner1.withdraw(amount)
    except ValueError:
        print("Please enter a valid number.")
else:
    print("Invalid action. Please type 'deposit' or 'withdraw'.")

#exercise 5 i genuinely got confused so i just got direct output for both questions down below
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # List of integers
    
    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

# Example usage
student1 = Student("Aarav", [85, 90, 78, 92])
print(f"{student1.name}'s average marks: {student1.average():.2f}")

#exercise 6
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary  # Monthly salary
        self.department = department
    
    def annual_salary(self):
        return self.salary * 12

# Create multiple employees
employees = [
    Employee("Neha", 50000, "HR"),
    Employee("Ravi", 75000, "Engineering"),
    Employee("Priya", 60000, "Marketing")
]

# Calculate total payroll
total_payroll = sum(emp.annual_salary() for emp in employees)

# Display results
for emp in employees:
    print(f"{emp.name} ({emp.department}) - Annual Salary: ₹{emp.annual_salary()}")

print(f"\nTotal Payroll for all employees: ₹{total_payroll}")
