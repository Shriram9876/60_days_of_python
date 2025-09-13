#exercise 1
import json

json_str = '{"city": "Berlin", "population": 3769000}'

with open("F:\python files\json_convertion","w")as e:
    json.dump(json_str,e)

with open("F:\python files\json_convertion","r")as e:
    content = json.load(e)

print(content)

import json

json_str = '{"city": "Berlin", "population": 3769000}'

# Convert JSON string to Python dictionary
data = json.loads(json_str)

# Save dictionary to file
with open("F:\\python files\\json_convertion", "w") as e:
    json.dump(data, e)

# Read dictionary back from file
with open("F:\\python files\\json_convertion", "r") as e:
    content = json.load(e)

print(content)

#exercise 2
import json

book_details = {
    "title": "The Silent Observer",
    "author": "Ananya Rao",
    "year": 2021,
    "publisher": {
        "name": "Lotus Press",
        "city": "Chennai"
    }
}

with open(r'F:\\python files\\book.json','w')as file:
    json.dump(book_details,file,indent=4)

#exercise 3
import json

student = [
    {
        "name": "Aarav Mehta",
        "grade": "A"
    },
    {
        "name": "Diya Sharma",
        "grade": "B+"
    },
    {
        "name": "Kabir Iyer",
        "grade": "A-"
    }
]

with open("F:\python files\student.json","w")as file:
    json.dump(student,file,indent=4)

with open("F:\python files\student.json","r")as file:
    student1 = json.load(file)

student1.append({"name": "Bob", "grade": "B"})

with open("F:\python files\student.json","w")as file:
    json.dump(student1,file,indent=4)

#exercise 4
import json

employees = [
    {
        "name": "Ravi Kumar",
        "salary": 75000
    },
    {
        "name": "Sneha Reddy",
        "salary": 82000
    },
    {
        "name": "Arjun Mehta",
        "salary": 91000
    },
    {
        "name": "Fatima Noor",
        "salary": 88000
    }
]

highest_paid = max(employees, key=lambda x: x["salary"])#this part was not done by me but to some extent i can this
print(f"The employee with the highest salary: {highest_paid}")

#exercise 5
company = {
  "company": "TechCorp",
  "departments": {
    "IT": {"employees": ["Alice", "Bob"]},
    "HR": {"employees": ["Charlie"]}
  }
}

print(company["company"]["employees"])

company = {
    "company": "TechCorp",
    "departments": {
        "IT": {"employees": ["Alice", "Bob"]},
        "HR": {"employees": ["Charlie"]}
    }
}

# Collect all employees
all_employees = []
for dept in company["departments"].values():
    all_employees.extend(dept["employees"])

print("All employees:", all_employees)

#exercise 6
import json

def safe_load_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' does not contain valid JSON.")
    except Exception as e:
        print(f"Unexpected error: {e}")