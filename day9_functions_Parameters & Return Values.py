#exercise 1
def square(num):
    return num*num

num1 = float(input("enter a number: "))
print(square(num1))

# exercise 2
def sum(a,b):
    return a+b

num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
print(sum(num1,num2))

#exercise 3 here with "for statement" i was trying to limit the numbers to sum up emphasis on "trying" it didn't work
"""def max_min(*num):
    total = 0
    for i in range(5):
        total += num
    return total


num2 = []
num1 = input("enter a list of number: ")
num2 += num1
print(int(max_min(num2)))"""
#this was wrong as i was reading 2 different questions together like for first part of the code it was one question and second part was different question so that's why i didn't work
"""def max_min(*num):
    total = 0
    for n in num:
        total += n
    return max(total), min(total)

print(max_min(2,4,5,6,7))"""
#this was the answer, the question was to find out maximum and minimum in given set of numbers ( i did that same mistake for codes above of exercise 3, reading the question wrongly)
def max_min(num):
    return max(num), min(num)

print(max_min([2,4,5,6,7]))

#exercise 4
def average(*num):
    return sum(num)/len(num)

print(average(3,3,3,21))

#exercise 5
def student_report(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print(student_report(name='maximus',age=16,grade='+A'))

#exercise 6 the GCD is from yesterday exercise question and i had to copy LCM because i forgot about arithmethatics
def is_divisor(n, d):
    return n % d == 0   # True if d divides n, False otherwise

def GCD(num1, num2):
    gcd = 1
    # check every number up to the smaller of the two
    for d in range(1, min(num1, num2) + 1):
        if is_divisor(num1, d) and is_divisor(num2, d):
            gcd = d   # update gcd if d divides both
    return gcd
num5 = int(input("enter a number: "))
num6 = int(input("enter a number: "))
print(GCD(num5,num6))

def LCM(a,b):
    return a*b // GCD(num5,num6)


print(f"LCM of two numbers is {LCM(num5,num6)}")
