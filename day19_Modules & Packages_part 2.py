#exercise 1
import sys

print(sys.version)
print(sys.argv)

#exercise 2
import subprocess

echo = subprocess.run(["echo", "learning python"], capture_output=True, text=True, shell=True)
print(echo.stdout)

#exercise 3
from collections import Counter

counts = Counter("the quick brown fox jumps over the lazy dog the quick fox")
print(counts)

#exercise 4
from collections import namedtuple

student = namedtuple("student", "name age grade")

student1 = student("john", 20, "completed college")

print(student1.name, student1.age, student1.grade)

#exercise 5 the code i wrote for the exercise
import itertools

num = [1, 2, 3, 4, 5]

num1 = list(itertools.combinations(num,2))

num1 = sum(num1)

print(num1)
#ans for the exercise
import itertools

num = [1, 2, 3, 4, 5]

# Generate all 2-element combinations
pairs = itertools.combinations(num, 2)

# Sum each individual pair
pair_sums = [a + b for a, b in pairs]

print(pair_sums)

#exercise 6
import sys

num1 = int(input("enter a number: "))
num2 = int(input("enter a numbre: "))

print(sys.argv)

import sys
#the answer
# sys.argv[0] is the script name, so we take sys.argv[1] and sys.argv[2]
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Print the sum
print(f"The sum of {num1} and {num2} is {num1 + num2}")