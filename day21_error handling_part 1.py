#exercise 1
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

try:
    num = num1/num2
except ZeroDivisionError:
    print("the denominator cannot be zero!")

#exercise 2
num1 = input("enter a number: ")

try:
    num = int(num1)
except ValueError:
    print("you have entered invalid value")

#exercise 3
file_name = input("enter the file name: ")

try:
    with open(file_name,"r")as file:
        content = file.read()
except FileNotFoundError:
    print("file not the found")

#exercise 4
file_name = input("enter the file name: ")

try:
    with open(file_name,"r")as file:
        content = file.read()
except FileNotFoundError:
    print("file not the found")
except PermissionError:
    print("the file cannot be accessed")

#exercise 5 just know that i didn't understand where to even start but i had a rough idea to do it
def calculator(a, b, op):
    try:
        a = float(a)
        b = float(b)
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        else:
            raise ValueError("Invalid operator")
    except ZeroDivisionError:
        return "Error: Division by zero"
    except ValueError as e:
        return f"Error: {e}"

# Sample runs
print(calculator(10, 5, "+"))
print(calculator(10, 0, "/"))
print(calculator("abc", 3, "*"))
print(calculator(8, 2, "^"))

#exercise 6 but this i straight up didn't get it 
def safe_int_convert(values):
    result = []
    for v in values:
        try:
            result.append(int(v))
        except ValueError:
            # skip invalid values
            pass
    return result

# Sample run
data = ["10", "20", "abc", "30", "4.5", "xyz"]
print(safe_int_convert(data))