#exercise 1
student_names = ("apful", "banane", "cherry", "date", "erdbereen","apful")
print(student_names)
print(student_names[2])

#exercise 2
num = [1,2,2,3,4,4,5]
print(num)
num = set(num)
print(num)

#exercise 3
def max_min(num1):
    return max(num1), min(num1)

print(max_min((1,2,2,3,4,4,5)))

#exercise 4
fusball = {"max","lisa","ali","peter","mia"}
basketball = {"lisa", "kurt", "mia", "zoey", "max"}
print(fusball.intersection(basketball))

#exercise 5 this was my attempt
names = {}
if command == "stop":
    name = input("ente a name: ")
    names.add(name)
    command = input("enter the code to stop: ")

print(sorted(names))

names = set()   # empty set

#this is the corrext for this exercise
while True:
    name = input("Enter a name (or type 'stop' to finish): ").lower()
    if name == "stop":
        break
    names.add(name)

print("Unique names:", sorted(names))

#exercise 6 the question so absurd i rather get the answer try to understand by looking at it
import random

def get_user_numbers():
    while True:
        raw = input("Enter 6 numbers between 1 and 40 (comma or space separated): ")
        try:
            tokens = raw.replace(",", " ").split()
            user = {int(x) for x in tokens}
        except ValueError:
            print("❌ Please enter only integers.")
            continue

        if len(tokens) != 6:
            print("❌ Please enter exactly 6 numbers.")
            continue

        if len(user) != 6:
            print("❌ Numbers must be unique (no duplicates).")
            continue

        if not all(1 <= n <= 40 for n in user):
            print("❌ All numbers must be between 1 and 40.")
            continue

        return user

def main():
    computer = set(random.sample(range(1, 41), 6))  # 6 unique numbers
    user = get_user_numbers()

    matches = user & computer

    print("\n--- Results ---")
    print("Computer numbers:", sorted(computer))
    print("Your numbers    :", sorted(user))
    print("Matches         :", sorted(matches))
    print("Total matches   :", len(matches))

if __name__ == "__main__":
    main()