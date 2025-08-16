#exercise 1
num = int(input("enter a number: "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")

#exercise 2
age = int(input("enter your age: "))
if age >= 18:
    print("you are an adult")
else:
    print("you are a minor")

#exercise 3
num = int(input("enter a number: "))
if num > 0 :
    print("the number is positive")
elif num < 0:
    print("the number is negative")
else:
    print("the number is zero")

#exercise 4
sentence = input("enter a anything: ")
print(bool(sentence))

#exercise 5
grade = int(input("enter your grade: "))
if grade > 90:
    print("grade is A")
elif grade < 90  and grade >= 80:
    print("grade is B")
elif grade < 80 and grade >= 70:
    print("grade is C")
elif grade < 70 and grade >= 60:
    print("grade is D")
else:
    print("grade is F")

#exercise 6  (i was pretty confused how to get it so just got answer for it)
# Get input from the user
day = input("Enter the day of the week: ").strip().capitalize()

# Check the day and print whether it's a weekday or weekend
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print(f"{day} is a weekday.")
elif day in ["Saturday", "Sunday"]:
    print(f"{day} is a weekend.")
else:
    print("Invalid day entered. Please check your spelling.")