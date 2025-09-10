#exercise 1
with open("notes2.txt",'w')as file:
    file.write("abcdef")

with open("notes2.txt","r")as file:
    content1 = file.read(3)
    print(file.tell())
    content2 = file.read()

print(content1)
print(content2)

#exercise 2
with open("notes.txt",'w')as file: 
    file.writelines(["line\n","line2\n","line3\n"])

with open("notes.txt",'r')as file: 
    for line in file: 
        print(line)

#exercise 3
with open("F:\\python files\\quotes.txt","w")as file:
    file.writelines(["line1\n","line2\n","line3\n"])

with open("F:\\python files\\quotes.txt","r")as file:
    content = file.read()

print(content)

#exercise 4
with open("F:\\python files\\filepointer.txt","w")as file:
    file.write("Python is amazing!")

with open("example.txt", "r") as file:
    first_six = file.read(6)
    print("First 6 characters:", first_six)

    position = file.tell()
    print("Current pointer position:", position)

    # Use seek(7) and read from there to the end
    file.seek(7)
    rest = file.read()
    print("Content from position 7 to end:", rest)

#exercise 5
with open("F:\\python files\\quotes.txt","r")as file:
    content = file.read()

with open("F:\\python files\\quotes1.txt","w")as file:
    file.write(content)

#exercise 6
with open("C:\\Users\\Asus\\Pictures\\Screenshot (5).jpg","rb")as file:
    content = file.read()

with open("F:\python files\copy_screenshot(5).jpg","wb")as file:
    file.write(content)