#exercise 1
import json

data = {
    "name": "schmidt",
    "age": 23,
    "hobbies": ["lesen", "coding"]   # better to store hobbies as a list
}

with open(r"F:\python files\me.json", "w") as f:
    json.dump(data, f, indent=4)

#exercise2 
import json

data = '{"title": "Inception", "year": 2010, "genres": ["Sci-Fi", "Thriller"]}'

json_str = json.loads(data)
print(json_str["title"])
print(json_str["genres"])

#exercise 3
import json

students = {
  "name": "John",
  "grade": "A",
  "subjects": ["Math", "Science", "History"]
}

# Write the dictionary to a JSON file
with open("student.json", "w") as file:
    json.dump(students, file)

# Read the JSON file back into a Python dictionary
with open("student.json", "r") as file:
    data = json.load(file)

print(data)

#exercise 4 i didn't get how to write this code
import json

# Step 1: Create a list of employee dictionaries
employees = [
    {"id": 101, "name": "Alice", "salary": 72000},
    {"id": 102, "name": "Bob", "salary": 48000},
    {"id": 103, "name": "Charlie", "salary": 53000}
]

# Step 2: Save the list to employees.json
with open("employees.json", "w") as file:
    json.dump(employees, file)

# Step 3: Reload the data from the file
with open("employees.json", "r") as file:
    loaded_employees = json.load(file)

# Step 4: Print names of employees with salary > 50,000
print("Employees with salary > 50,000:")
for emp in loaded_employees:
    if emp["salary"] > 50000:
        print(emp["name"])