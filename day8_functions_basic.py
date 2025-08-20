#exercise 1
print("hello world!")

#exercise 2
def even_odd(num):
    if num % 2 == 0:
        return "number is even"
    else:
        return "number is odd"

num2 = int(input("enter a number: "))
num1 = even_odd(num2)
print(num1)

#exercise 3 (even this i got till for statement but after that i don't know what to do)
Vowels = ['a','e','i','o','u']
def vowels(word):
    count = 0
    for ch in word:
        if ch in Vowels:
            count += 1
    return count

words = input("enter a word: ")
print(vowels(words))

#exercise 4 this is the question i am so confused by it(Write a function that takes two numbers and returns their greatest common divisor (GCD).)
def is_divisor(n, d):
    return n % d == 0   # True if d divides n, False otherwise

def GCD(num1, num2):
    gcd = 1
    # check every number up to the smaller of the two
    for d in range(1, min(num1, num2) + 1):
        if is_divisor(num1, d) and is_divisor(num2, d):
            gcd = d   # update gcd if d divides both
    return gcd
num5 = int(input("enter a number: "))
num6 = int(input("enter a number: "))
print(GCD(num5,num6))

#exercise 5 this was also confusing as a i was unaware of what fibonacci series was... now i know
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

print(generate_fibonacci(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#exercise 6
Symbols = input("enter any of these symbols(+,-,*,/): ")
def calculator(a,b):
    if Symbols == "+":
        return a + b
    elif Symbols == "-":
        return a - b
    elif Symbols == "*":
        return a * b
    elif Symbols == "/":
        return a / b
    pass

num2 = float(input("enter a number: "))
num1 = float(input("enter a number: "))

print(calculator(num1,num2))
