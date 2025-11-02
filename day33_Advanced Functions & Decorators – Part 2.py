#exercise 1
def add_number(n):
    def addition(x):
        return x + n
    return addition

add5 = add_number(5)
print(add5(10))  # Output: 15

#exercise 2
def text1(text):
    return text.upper()

def greet(func):
    message = func("hallo leute!")
    print(message)

greet(text1)

def text1(text):
    def greet(func):
        def wrapper():
            return text.upper()
        return wrapper
    return greet

@text1("python")
def sayname():
    return "This won't be used"

print(sayname())

#exercise 3
def positive_numbers(num):
    def wrapper(num1):
        if num1 < 0:
            print("the number is negative")
        else:
            print("the number is positive")
            return
        return num(num1)
    return wrapper

@positive_numbers
def print_square(num1):
    return "nothing here"

print_square(4)
print_square(-3)