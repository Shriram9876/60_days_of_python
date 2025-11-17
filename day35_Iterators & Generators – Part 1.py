#exercise 1
nums = [2, 4, 6, 8]

it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#exercise 2
def is_iterable(obj):
        try:
            iter(obj)
            print("the obj1 is iterable")
        except TypeError:
            print("the obj1 is not iterable")
            
obj1= 42 #tuple() even if they are empty they can be iterable
is_iterable(obj1)

nums = [2, 4, 6, 8]
is_iterable(nums)

#exercise 3
#my attempt
class EvenNumbers:
    def __init__(self,max):
        self.max = max
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.max:
            if self.count % 2 == 0:
                self.count += 1
                return self.count
            return StopIteration


for n in EvenNumbers(10):
    print(n)

class EvenNumbers:
    def __init__(self, max):
        self.max = max
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.count < self.max:
            current = self.count
            self.count += 1
            if current % 2 == 0:
                return current
        raise StopIteration

# Test
for n in EvenNumbers(10):
    print(n)

#exercise 4
class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data)  # Start from the end

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Example usage:
for item in ReverseList([10, 20, 30]):
    print(item)

#exercise 5
class InfiniteCounter:
    def __init__(self,count):
        self.count = count
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.count += 1
        return self.count

counter = InfiniteCounter(100)
print(next(counter))   # 100
print(next(counter))   # 101

#exercise 6
class Fibonacci:
    def __init__(self):
        self.a = 0  # F(0)
        self.b = 1  # F(1)

    def __iter__(self):
        return self

    def __next__(self):
        value = self.a
        self.a, self.b = self.b, self.a + self.b  # Update to next pair
        return value

# Example usage:
fib = Fibonacci()
for _ in range(10):
    print(next(fib))