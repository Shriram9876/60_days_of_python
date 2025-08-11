print("hallo python")

name = input("enter deine name: ")
age = int(input("enter deine age: "))
stadt = input("enter your city: ")
print(name,age,stadt)
print(type(name))
print(type(age))
print(type(stadt))

number = 34
print(type(number))

print(f"name is {name}, \n age is {age}, \n{stadt}")

#output
"""
lukas 23 munchen
<class 'str'>   
<class 'int'>   
<class 'str'>   
<class 'int'>   
name is lukas,  
 age is 23,     
munchen
"""