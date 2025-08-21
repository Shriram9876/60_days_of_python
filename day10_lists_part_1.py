#exercise 1
num = [1,2,3,4,5]

print(num[0])
print(num[-1])

#exercise 2
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)
fruits.remove("banana")
print(fruits)

#exercise 3 first one is single input one and i didn't know how to get multiple input so i had look it up 
num = []

while True:
    num1 = int(input("enter a set of numbers: "))
    if num1 % 2 == 0:
        num.append(num1)
    break

print(sorted(num))

num = []
limit = int(input('set the number limit for the list: '))   # set how many numbers you want

for i in range(limit):
    num1 = int(input(f"Enter number {i+1}: "))
    if num1 % 2 == 0:
        num.append(num1)

print(sorted(num))

#exercise 4
student_names = ["apple", "banana", "cherry", "date","erdbereen"]
print(student_names)
student_names[1] = "rahul"
print(student_names)

#exercise 5 this was my attempt 
num = [1,2,3,4,5]
student_names = ["apple", "banana", "cherry", "date","erdbereen"]
lists = []
lists.append(num)
lists.append(student_names)
print(lists)

#and this was the answer again i am being narrow minded only using tools from certain days only
num = [1, 2, 3, 4, 5]
student_names = ["apple", "banana", "cherry", "date", "erdbereen"]

# 1. Merge the two lists
merged = num + student_names

# 2. Remove duplicates by converting to set, then back to list
merged = list(set(merged))

# 3. Sort the list
merged.sort()

print(merged)

#exercise 6
student_names = [10, 20, 30, 40, 50]
lists = []
lists.append(student_names[-1])
lists.append(student_names[3])
lists.append(student_names[2])
lists.append(student_names[1])
lists.append(student_names[0])
print(lists)