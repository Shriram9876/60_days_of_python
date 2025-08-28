#exercise 1
lerter = input("enter a word: ").lower()
print(lerter.startswith("py"))

#exercise 2
sentence = input("enter a sentence: ").lower()
print(sentence.count("e"))

#exercise 3
sentence = input("enter a sentence: ")
if sentence.isdigit():
    print("valid number")
else:
    print("not a valid number")

#exercise 4
file_name = input("enter the file name: ").lower()
print(file_name.endswith(".txt") or file_name.endswith(".pdf"))

#exercise 5 (this is my attempt at the code)
sentence = input("enter a sentence: ").lower()
if sentence.find("python"):
    print(sentence.find("python"))
else:
    print('not found')

# this is the answer for this exercise
sentence = input("Enter a sentence: ").lower()

index = sentence.find("python")

if index != -1:
    print(f"'python' found at index {index}")
else:
    print("Not found")

#exercise 6
name = input("enter your name: ")
age = int(input("enter your age: "))
print(f"ich bin {name}, und ich bin {age} jahre alt")