#exercise 1
for i in range(1,11):
    if i == 6:
        break
    print(i)

#exercise 2
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#exercise 3 (this was my attempt but i am still having hard time understanding 'while' which confusing me a fair bit)
"""num = int(input('enter a number: '))
while num == 0:
    break
print("yes the number you have entered is zero")"""
#here is the answer supposed to like (the question was loop the user input until you get 0 after that it should break)
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Stopping… bye!")
        break
    print("You entered:", num)

#exercise 4
num = [1,2,3,4,5,6,7,8,9]
for i in num:
    if i % 2 != 0:
        continue
    print(i)

#exercise 5 (even this one was confusing as it asked me to use breal & any to find out any negative numbers present in the loop and i got confused on using any() and i am noticing that boolean is being frequently in the loops)
num = [2,3,4,65,7,2,-44,3]

found_negative = False

for n in num:
    if any([n < 0]):
        found_negative = True
        break
    
if found_negative:
    print("negative number is found")

#exercise 6
while True:
    password = "secret123"
    Password = input("enter your password: ")
    if password == Password:
        break
print("welkomen user")

#exercise 7
while True:
    even_number = False
    even = int(input("enter a number: "))
    condition = even % 2 == 0
    if any([condition]):
        even_number = True
        break

if even_number:
    print("even number found")

#execise 8
"""while True:
    positive_number = False
    num = int(input("enter any number: "))
    if num <= 0:
        continue
    else:
        positive_number =True
        
if positive_number:
    print(num)"""
#here is the corrected version and this was the question
"""Keep asking the user for input until they type a number greater than 0.

If they enter 0 or a negative number, use continue to skip to the next loop iteration.

Use a boolean flag to confirm if a valid number has been entered, and then stop the loop."""
while True:
    num = int(input("enter any number (0 to stop): "))
    
    if num <= 0:
        continue   # skip negatives and zero
    else:
        print("You entered a positive number:", num)
        break       # stop the loop after finding the first positive number

# exercise 9 (this is my attempt)
"""num = [1,2,4,-3]

while True:
    if all([i < 0 for i in num]):
        print("not all numbers are positve")
        break"""
#this is the answer
num = [1, 2, 4, -3]

while True:
    if all([n > 0 for n in num]):
        print("All numbers are positive")
    else:
        print("Not all numbers are positive")
    break   # exit loop after one check

#exercise 9 (i couldn't even try to attempt to write the code for the question so just got straight answer and try to understand)
while True:
    password = input("Enter your password: ")

    # Check all rules using any() and all()
    if len(password) < 6:
        print("Password must be at least 6 characters long.")
        continue

    if not any(char.isdigit() for char in password): #this line is straight up confusing because i don't even how it works
        print("Password must contain at least one digit.")
        continue

    if not any(char.isupper() for char in password): #same goes for this too
        print("Password must contain at least one uppercase letter.")
        continue

    print("Password accepted!")
    break