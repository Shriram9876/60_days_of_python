#exercise 1
import csv

rows = [
    ["name", "salary(1k)"],
    ["Alice", 95],
    ["Bob", 88]
]

with open("F:\python files\data_semicolon.csv","w",newline="")as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(rows)

with open("F:\python files\data_semicolon.csv","r")as file:
    contain = csv.reader(file, delimiter=";")
    for con in contain:
        print(con)

#exercise 2
import csv 

rows = [
    ["name", "salary(1k)"],
    ["Charlie", 102],
    ["Dana", 76],
    ["Eli", 89]
]

with open("F:\python files\data.tsv","w",newline="")as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(rows)

with open("F:\python files\data.tsv","r")as file:
    contain = csv.reader(file, delimiter="\t")
    for con in contain:
        print(con)

#exercise 3
import csv

rows = [
    ["username", "comment"],
    ["alice", "Great job!"],
    ["bob", "Well done, keep it up!"],
    ["charlie", "Needs improvement."]
]

with open("F:\python files\comments.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("F:\python files\comments.csv", "r") as file:
    Convert = csv.reader(file, quotechar='"')
    for conve in Convert:
        print(conve)

#exercise 4
import csv

rows = [
    ["ID", "Value1", "Value2", "Value3"],
    [1, 23, 45, 67],
    [2, 89, 12, 34],
    [3, 56, 78, 90]
]

with open("F:\\python files\\numbers.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerows(rows)

with open("F:\\python files\\numbers.csv", "r") as file:
    Convert = csv.reader(file, delimiter="\t")
    next(Convert)  # Skip header row

    total = 0
    for conve in Convert:
        total += int(conve[1])
        print("sum of values of column 1 is: ", total )

#exercise 5
import csv

rows1 = []

rows = [
    ["product", "price", "quantity"],
    ["Laptop", 75000, 5],
    ["Smartphone", 30000, 10],
    ["Headphones", 1500, 25]
]

with open("F:\\python files\\sales.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(rows)

with open("F:\\python files\\sales.csv", "r") as file:
    contain = csv.reader(file, delimiter=";")
    next(contain)

    for conve in contain:
        if int(conve[1]) > 100:
            rows1.append(conve[0])

with open("F:\\python files\\high_sales.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(rows1)

#exercise 6
import csv

rows = [
    ["name", "age", "marks"],
    ["Aarav", 17, 88],
    ["Diya", 16, 92],
    ["Kabir", 18, 75]
]

with open("F:\\python files\\students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with open("F:\\python files\\students.csv", "r") as file:
    contain = csv.reader(file, delimiter=";")
    next(contain)

    total = 0
    for conve in contain:
        total1 = sum(int(conve[2]))/len(int(conve[2]))
        total += total1

print(total)

import csv

rows = [
    ["name", "age", "marks"],
    ["Aarav", 17, 88],
    ["Diya", 16, 92],
    ["Kabir", 18, 75]
]

# Write to students.csv
with open("F:\\python files\\students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

# Read and calculate average of marks
with open("F:\\python files\\students.csv", "r") as file:
    contain = csv.reader(file)
    next(contain)  # Skip header

    total = 0
    count = 0
    for conve in contain:
        total += int(conve[2])
        count += 1

average = total / count
print("Average marks:", average)