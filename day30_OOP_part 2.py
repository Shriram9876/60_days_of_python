#exercise 1
class animal:
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} here is your food, come and eat")

class dog(animal):
    def bark(self):
        print(f"{self.name} bark for me.")

dog1 = dog("germanshephard")
dog1.eat()
dog1.bark()

#exercise 2
class vehicle:
    def __init__(self,car_name):
        self.car_name = car_name
    
    def drive(self):
        print(f"{self.car_name} is not driving")

car1 = vehicle("porsche")
car1.drive()

class car(vehicle):
    def drive(self):
        print(f"{self.car_name} is driving")

car2 = car("porsche")
car2.drive()

#exercise 3
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
class Student(person):
    def __init__(self,name,age,Student_id):
        super().__init__(name,age)
        self.Student_id = Student_id
    
    def Student_id1(self):
        print(f"{self.name} is {self.age} years old and their student ID is {self.Student_id}")

student1 = Student("eddy",15,2421445)
student1.Student_id1()

#exercise 4
class grandparents:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"{self.name} is their name and their age is {self.age}")

class parents(grandparents):
    def show(self):
        print(f"{self.name} is their name and their age is {self.age}")

class children(parents):
    def show(self):
        print(f"{self.name} is their name and their age is {self.age}")

groseltern = grandparents("karl",50)
groseltern.show()

eltern = parents("anna", 34)
eltern.show()

kinder = children("max",5)
kinder.show()

#exercise 5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def approve_leave(self):
        print(f"{self.name}, your leave is approved.")

class Developer(Employee):
    def write_code(self):
        print(f"{self.name} is currently developing a different project.")

# Creating instances
employees = Manager("Harry", 22000)
employees.approve_leave()

employee = Developer("Barry", 36000)
employee.write_code()

#exercise 6
class account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class savingsaccount(account):
    def savings(self):
        interest = self.balance * 2 / 100
        self.balance += interest
        print(f"Your current balance in your savings account is ₹{self.balance:.2f}")

# i used AI for this part alone as i was confused to produce the current output which is being displayed 
class checkingaccount(account):
    def withdraw(self, amount):
        self.balance -= amount
        print(f"₹{amount:.2f} has been withdrawn from your account.")

        if self.balance < 0:
            overdraft_fee = abs(self.balance) * 0.05  # 5% overdraft fee
            print(f"⚠️ Your account is overdrawn by ₹{abs(self.balance):.2f}")
            print(f"💸 Overdraft fee to be paid: ₹{overdraft_fee:.2f}")
        else:
            print(f"✅ Your current balance is ₹{self.balance:.2f}")

# 🧪 Example usage
print("=== Checking Account Transaction ===")
owner_name = "Ravi"
initial_balance = 1000
withdraw_amount = 1200

chk_acc = checkingaccount(owner_name, initial_balance)
chk_acc.withdraw(withdraw_amount)