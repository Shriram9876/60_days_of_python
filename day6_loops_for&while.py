#exercise 1
for i in range(1,11):
    print(i)

#exercise 2
n = 5
while n >= 1:
    print("the numbers between 6 and 0: ", n )
    n -= 1

#exercise 3
for i in range(0,21,2):
    print(i)
# or
for i in range(1,21):
    if i % 2 == 0:
        print(i)

#exercise 4 (this is the answer i thought would work but it was wrong)
num = int(input("enter a number: "))
while n in range(num):
    n += 1
    print(n)
# this was the correct answer apparently
num = int(input("Enter a number: "))

n = 1          # start counting from 1
total = 0      # to hold the running sum

while n <= num:   # loop until we reach num
    total += n    # add current n to sum
    n += 1        # move to next number

print("Sum from 1 to", num, "is:", total)

#exercise 5
num = int(input('enter a number: '))
for i in range(1,11):
    n = i*num
    print(n)

#exercise 6
name = ["maria", "peter", "moritz", "wolfgang"]
score = [32,55,78,58,90]
for n,s in zip(name,score):
    print(n,s)

#exercise 7
fruits = ["apple", "banana", "cherry", "date"]
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")