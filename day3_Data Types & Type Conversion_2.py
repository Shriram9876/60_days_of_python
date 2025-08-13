#exercise 2
num1 = "45"

num = int(num1)

print(num)

num2 = str(num)

print(num2)

num3 = float(num2)
print(num3)

#exercise 3
num1 = input("enter a number: ")
num2 = input("enter a number: ")

num3 = float(num1) + float(num2)

print(num3)

#exercise 4
data = {
    "name": "Eddy",
    "age": 25,
    "height": 5.9,
    "is_student": True
}
data1 = str(data)
print(data1)

#exercise 4 (this was the correct answer)
data = {
    "name": "Eddy",
    "age": 25,
    "height": 5.9,
    "is_student": True
}

# Convert values to strings
for key in data:
    data[key] = str(data[key])

print(data)