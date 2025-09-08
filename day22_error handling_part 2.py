#exercise 1
num1 = int(input("enter a number: "))

try:
    num = num1*num1
except ValueError:
    print("enter number only!")
else:
    print(num)

#exercise 2
num1 = int(input("enter a number: "))

try:
    num = num1*num1
except ValueError:
    print("enter number only!")
else:
    print(num)
finally:
    print("done")

#exercise 3
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

balance = 500
amount = int(input("Enter the amount to be withdrawn: "))

try:
    actual_bal = withdraw(balance, amount)
except ValueError as e:
    print(e)
else:
    print(f"You have withdrawn successfully. The amount left in the account is: {actual_bal}")
finally:
    print("Thank you for operating")

#exercise 4
file = None
try:
    file = open("text.txt", "r")
except FileNotFoundError:
    print("the file is not available")
else:
    content = file.read()
    print(content)
finally:
    if file:
        file.close()

try:
    with open("text.txt","r")as file:
        content = file.read()
except FileNotFoundError:
    print("the file is not available")
else:
    print(content)

#exercise 5
class InvalidAgeError(Exception):
    pass

def eligble_vote(age):
    if age < 18:
        raise InvalidAgeError("the person is ineligable to vote")

age = int(input("enter your age: "))

try:
    eligble_vote(age)
except InvalidAgeError as ew:
    print(ew)
else:
    print(f"the person is above 18 therefore is elgible to vote.")

#exercise 6
NuM = [1, 2, 3, 4, 5]

class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot take square root of negative number")
    return x ** 0.5

for num in NuM:
    try:
        result = square_root(num)
        print(f"Square root of {num} is {result}")
    except NegativeNumberError as aw:
        print(f"Error for {num}: {aw}")
