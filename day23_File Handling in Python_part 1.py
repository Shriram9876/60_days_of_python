#exercise 1
file = open("notes.txt",'x')
file.close()

with open("notes.txt","w")as file:
    file.write("Learning Python File Handling!")

#exercise 2
file = open("notes.txt",'x')
file.close()

with open("notes.txt","w")as file:
    file.write("Learning Python File Handling!")

with open("notes.txt","r")as file:
    content = file.read()

print(content)

#exercise 3
with open("F:\\python.py\\notes.txt","a")as file:
    file.writelines(["In python i like error handling\n", "In python i like ifelse and loops\n", "In python i do not like list comprehensions\n"])

#exercise 4
with open("F:\\python.py\\notes.txt","r")as file:
    content = file.readlines()
    number_lines = len(content)

print(number_lines)

#exercise 5
with open("F:\\python.py\\notes.txt","r")as file:
    content = file.read()

with open("F:\\python.py\\backup_notes.txt","w")as file:
    file.write(content)

#exercise 6 i didn't understand how to write this code
# Open the file in read mode
with open("F:\\python.py\\notes.txt", "r") as file:
    # Read all lines into a list
    lines = file.readlines()

# Find the longest line using max() with key=len
longest_line = max(lines, key=len)

# Print the longest line (with trailing newline removed)
print("Longest line:")
print(longest_line.strip())