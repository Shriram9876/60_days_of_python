#exercise 1
student_names = {
    "markus" : "schwarz",
    "maria" : "weis",
    "may" : "rot"
}
print(student_names)
student_names.update({"may":"weich rot", "max": "rot"})
print(student_names)

#exercise 2
print(student_names.pop("may"))

#exerccise 3
stadt = {
    "munchen" : "funf million",
    "berlin" : "elf million",
    "zurich" : "acht million",
}

stadt2 = stadt.copy()
stadt.clear()
print(stadt)
print(stadt2)

#exercise 4
cubes = {x: x*x*x for x in range(1,11)}
print(cubes)

#exercise 5
products = {
    "bucherregal" : "$500",
    "tisch" : "$440",
    "bucher" : "$30",
    "fernseher" :  "$8000"
}

print(products)

products.popitem()

print(products)

#exercise 6 this down here is the my attempt at exercise 
for i in range(1,5):
    i = input("enter a word: ")
    sprechen = 0
    sprechen += i

words = {sprechen: len(sprechen)}

print(words)

# Collect 5 words from user (and this was the answer)
words_list = []

for _ in range(5):
    word = input("Enter a word: ")
    words_list.append(word)

# Build dictionary: word → length
words = {w: len(w) for w in words_list}

print(words)