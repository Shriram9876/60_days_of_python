#exercise 1
import math

print(math.sqrt(225))

#exercise 2
import random 

print(random.randint(50,100))

#exercise 3
from datetime import datetime

today = datetime.now()
print(today.strftime("%d-%m-%y"))

#exercise 4
import os

print(os.getcwd())

#exercise 5
import random

num = random.randint(1,6)
num1 = random.randint(1,6)
if num == num1:
    print(f"the number from dice 1: {num} and number from dice 2 is {num1}")
else:
    print(f"schade das nummers sind different {num}, {num1}")

#exercise 6
from datetime import datetime, timedelta

today = datetime.now()
past = today - timedelta(days=100)
future = today + timedelta(days=100)

print(f"100 days from current date: {future} and 100 days before current date: {past}")