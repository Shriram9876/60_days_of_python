#exercise 1
num = [1,2,3,4,5,6,7,8,9,10]
for i in num:
    if i % 2 == 0:
        num.remove(i)
print(num)

#exercise 2
student_names = ["apful", "banane", "cherry", "date", "erdbereen","apful"]
print(student_names.count("apful"))

#exercise 3 this is my attempt at the code 
"""def list_with_numbers(*num):
    return list(sort(num))
    return num.reverse()
    return f"here is the list in reverse order and in descending order too {num}"

print(num(23,46,78,997,343,6575))"""

#this is the corrected version of the above code 
def list_with_numbers(num_list):
    sorted_list = sorted(num_list)       # Step 1: sort ascending
    descending = sorted_list[::-1]       # Step 2: reverse
    return descending

print(list_with_numbers([23, 46, 78, 997, 343, 6575]))

#exercise 4
sentence = input("enter a sentence: ")
sorted_list = list(sentence.strip())
print(sorted_list)

#exercise 5 this was the answer for this exercise
to_do_list = ["Day 8 functions", "Day 7 loop control", "Day 6 loop", "Day 9 parameters"]

while True:
    print("\nYour To-Do List:", to_do_list)
    action = input("Type 'add', 'remove', 'show', or 'exit': ").lower()

    if action == "add":
        task = input("Enter a new task: ")
        to_do_list.append(task)

    elif action == "remove":
        task = input("Enter the task to remove: ")
        if task in to_do_list:
            to_do_list.remove(task)
        else:
            print("Task not found.")

    elif action == "show":
        print("Current tasks:", to_do_list)

    elif action == "exit":
        print("Goodbye! Final tasks:", to_do_list)
        break

    else:
        print("Invalid choice. Try again.")
#my version is here
to_do_list = ("Day 8 functions",'day 7 loop control',"day 6 loop", "Day 9 parameters")
for day in to_do_list:
    to_do_list = list(day)
    order = input('enter a the password to stop the code: ').lower()
    if order == "exit":
        break
    break
    
print(to_do_list)

#exercise 6 this was the answer for this exercise 
import random

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
winner = []   # define once, before loop

for i in range(5):
    choice = random.choice(num)   # pick a number
    winner.append(choice)         # add it to winner list
    num.remove(choice)            # remove so no duplicates

winner = sorted(winner)   # sort once at the end
print("Lottery winners are:", winner)

#and this was my attempt
import random

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

winner = []

for i in range(5):
    winner.append(random.choice(num))
    winner = sorted(winner)

print(winner)