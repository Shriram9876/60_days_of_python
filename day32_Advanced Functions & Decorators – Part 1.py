#exercise 1
def outer_greeting(greet):
    def Personal(name):
        return f"{greet} {name}"
    return Personal

hello = outer_greeting("Hello")
print(hello("Alice"))

#exercise 2
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # 1
print(c())  # 2

#exercise 3
def make_multiplier(factor):
    def multiply_by(n):
        return factor*n
    return multiply_by

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Output: 10
print(triple(4))  # Output: 12

#exercise 4
def discount_calculator(discount):
    def price_after_discount(price):
        return price - discount
    return price_after_discount

summer_sale = discount_calculator(20)
print(summer_sale(100))  # 80.0

#exercise 5
def make_average():
    total = 0
    count = 0
    def add_number(num):
        nonlocal total, count
        total += num
        count += 1
        return total / count
    return add_number

# Example usage:
avg = make_average()
print(avg(10))  # Output: 10.0
print(avg(20))  # Output: 15.0
print(avg(30))  # Output: 20.0