#exercise 1
name = "alex"
print(name[0])
print(name[-1])

#exercise 2
sentence = input("enter a random sentence: ")
print(sentence.upper())
print(sentence.lower())

#exercise 3
sentence = input("Enter a random sentence now! : ")
cleaned = sentence.strip()
print(f"Length of cleaned sentence: {len(cleaned)}")

#as side note of when there is spaces between the sentences
sentence = input("Enter a random sentence now! : ")

# Remove leading/trailing + extra spaces in between
cleaned = " ".join(sentence.split())

print(f"Cleaned sentence: '{cleaned}'")
print(f"Length of cleaned sentence: {len(cleaned)}")

#exercise 4
sentence = input("enter a random sentence: ").lower()
print(sentence.replace("a","@"))

#exercise 5
sentence = input("enter a random: ")
print(sentence.split(","))

#exercise 6
words = []
for _ in range(5):
    wald = input("enter a word: ")
    words.append(wald)

print(" ".join(words))