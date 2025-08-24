#exercise 1
details = {
    "name" : "kurt",
    "age" : 20,
    "hobbys" : "learning"
}
print(details.keys())

#exercise 2
fruit_prices = {
    "apful" : "zweihundert",
    "orangen":"eins",
    "kartofflen": "dreisig",
    "Erdbeeren" : "funfundzwanzig"
}

print(fruit_prices.values())

#exercise 3
details = {
    "name" : "kurt",
    "age" : 20,
    "hobbys" : "learning"
}

fruit_prices = {
    "apful" : "zweihundert",
    "orangen":"eins",
    "kartofflen": "dreisig",
    "Erdbeeren" : "funfundzwanzig"
}

print(details["name"])
print(details["Name"])
print(fruit_prices.get("apful"))
print(fruit_prices.get("apful",'nicht frei'))
print(fruit_prices.get("appful", 'nicht frei'))

#exercise 4
fruit_prices = {
    "apful" : "zweihundert",
    "orangen":"eins",
    "kartofflen": "dreisig",
    "Erdbeeren" : "funfundzwanzig"
}

print(fruit_prices.items())

#exercise 5
student_names = {
    "markus" : 56,
    "maria" : 39,
    "may" : 90
}

for name, mark in student_names:
    if mark >= 40:
        print(f"{name} {mark} \n the above students have passed")
    else:
        print(f"{name} {mark} \n the above students have not passed")

#exercise 6  this is my attempt at the code
countries_capitals = {
    "deutschland" : "kein ahnung",
    "amerika" : "washington",
    "russland" : "moscow",
    "china" : "beijieng",
    "kanada" : "ontario"
}

country = input("enter a country name: ").lower()

if country == countries_capitals.keys():
    print(f"{countries_capitals.items}")
else:
    print("please enter the country within the list!")

#this is the answer 
countries_capitals = {
    "deutschland": "berlin",
    "amerika": "washington",
    "russland": "moscow",
    "china": "beijing",
    "kanada": "ottawa"
}

country = input("Enter a country name: ").lower()

if country in countries_capitals:
    print(f"The capital of {country} is {countries_capitals[country]}")
else:
    print("Please enter a country within the list!")