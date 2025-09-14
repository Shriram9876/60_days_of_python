#exercise 1
import csv

obst = [
    ['fruit','price'],
    ['kartoffeln','neunundneunzig'],
    ['apfel','dreizig'],
    ['gurken','vierzig']
]

with open("F:\python files\obst.csv","w",newline="")as file:
    list_obst = csv.writer(file)
    list_obst.writerows(obst)

with open("F:\python files\obst.csv","r")as file:
    list_obst1 = csv.reader(file)

print(list_obst1)

import csv

obst = [
    ['fruit', 'price'],
    ['kartoffeln', 'neunundneunzig'],
    ['apfel', 'dreizig'],
    ['gurken', 'vierzig']
]

# Use raw string for file path
with open(r"F:\python files\obst.csv", "w", newline="", encoding="utf-8") as file:
    list_obst = csv.writer(file)
    list_obst.writerows(obst)

# Read and print the contents properly
with open(r"F:\python files\obst.csv", "r", encoding="utf-8") as file:
    list_obst1 = csv.reader(file)
    for row in list_obst1:
        print(row)

#exercise 2
import csv

haustire = [
    ['name', 'animal', 'age'],
    ['ed','hund','neun'],
    ['moritz','eule','acht'],
    ['benna','elefant','elf']
]

with open(r"F:\\python files\\haustire.csv", "w", newline="", encoding="utf-8") as file:
    list_haustire = csv.writer(file)
    list_haustire.writerows(haustire)

#exercise 3
import csv

buchen = [
    ["title", "author", "year"],
    ["To Kill a Mockingbird", "Harper Lee", 1960],
    ["1984", "George Orwell", 1949],
    ["The Great Gatsby", "F. Scott Fitzgerald", 1925]
]

with open(r"F:\\python files\\buchen.csv", "w", newline="", encoding="utf-8") as file:
    list_buchen = csv.DictWriter(file)
    list_buchen.writerows(buchen)

import csv

# Convert list of lists to list of dictionaries
buchen = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

# Define the fieldnames explicitly
fieldnames = ["title", "author", "year"]

# Write to CSV using DictWriter
with open(r"F:\python files\buchen.csv", "w", newline="", encoding="utf-8") as file:
    list_buchen = csv.DictWriter(file, fieldnames=fieldnames)
    list_buchen.writeheader()           # Writes the header row
    list_buchen.writerows(buchen)       # Writes the data rows

#exercise 4
import csv

with open(r"F:\python files\buchen.csv", "r") as file:
    buch1 = csv.DictReader(file)
    for buch in buch1:
        print(buch['title'])

#exercise 5
import csv

# Step 1: Create sample student data
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"},
    {"name": "David", "age": 21, "grade": "C"},
    {"name": "Eva", "age": 20, "grade": "B"},
    {"name": "Frank", "age": 23, "grade": "A"}
]

# Step 2: Write to CSV file
with open(r"F:\python files\students.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

# Step 3: Read and filter students with grade "A"
with open(r"F:\python files\students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("Students with grade A:")
    for student in reader:
        if student["grade"] == "A":
            print(student["name"])

#exercise 6
import csv
import json

# Step 1: Read data from students.csv
students = []
with open(r"F:\python files\students.csv", "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        students.append(row)

# Step 2: Write data to students.json
with open(r"F:\python files\students.json", "w", encoding="utf-8") as json_file:
    json.dump(students, json_file, indent=4)