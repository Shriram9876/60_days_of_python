#exercise 1
name = 'eddy'
num1 = 4
num2 = 4.4
logical_values = True
print(type(name))
print(type(num1))
print(type(num2))
print(type(logical_values))

#output
"""
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
"""

#this one was the answer for this exercise
# Text type
name = 'eddy'

# Numeric types
num1 = 4
num2 = 4.4

# Boolean type
logical_values = True

# Collection types
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"key": "value"}

# Type checks
print(type(name))          # str
print(type(num1))          # int
print(type(num2))          # float
print(type(logical_values))# bool
print(type(my_list))       # list
print(type(my_tuple))      # tuple
print(type(my_set))        # set
print(type(my_dict))       # dict

#difference between mutable(changable) and immutable(unchangable)
# Immutable examples
print("\n--- Immutable Tests ---")

# str
name = "eddy"
try:
    name[0] = "E"
except TypeError as e:
    print("str:", e)

# int
num = 10
try:
    num[0] = 5
except TypeError as e:
    print("int:", e)

# float
flt = 3.14
try:
    flt[0] = 1.5
except TypeError as e:
    print("float:", e)

# bool
flag = True
try:
    flag[0] = False
except TypeError as e:
    print("bool:", e)

# tuple
tup = (1, 2, 3)
try:
    tup[0] = 99
except TypeError as e:
    print("tuple:", e)


print("\n--- Mutable Tests ---")

# list
my_list = [1, 2, 3]
my_list[0] = 99
print("list after change:", my_list)

# set
my_set = {1, 2, 3}
my_set.add(4)
print("set after add:", my_set)

# dict
my_dict = {"key": "value"}
my_dict["key"] = "new value"
print("dict after change:", my_dict)