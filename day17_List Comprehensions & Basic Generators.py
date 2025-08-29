#exercise 1
even_numbers = [i for i in range(1,21) if i % 2 == 0]
print(even_numbers)

#exercise 2 this was my attempt at the code
multiples_of_3 = (i for i in range(5) if i % 3 == 0)
print(multiples_of_3)

#this was the answer to the question
def generate_multiples_of_3():
    count = 0
    num = 1
    while count < 5:
        if num % 3 == 0:
            yield num
            count += 1
        num += 1

# Use the generator
for multiple in generate_multiples_of_3():
    print(multiple)

#exercise 3 this is my attempt at the code
x = "Python is fun"
sentence = [x for x in _.isalnum()]
print(sentence(len(x)))

#this is the answer for the question
x = "Python is fun"
sentence = [len(word) for word in x.split()]
print(sentence)

#exercise 4
def fibonacci_upto(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Example usage:
for num in fibonacci_upto(50):
    print(num, end=" ")

#exercise 5
nested = [[1,2],[3,4],[5,6]]
flattened = [num for sublist in nested for num in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6]

#exercise 6
def read_file_line_by_line(filepath):
    with open(filepath, "r") as file:
        for line in file:
            yield line.strip()  # yield each line without newline character

# Example usage (assuming "sample.txt" exists):
for line in read_file_line_by_line("sample.txt"):
    print(line)