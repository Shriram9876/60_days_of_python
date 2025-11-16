#exercise 1
class Temperature:
    def __init__(self,celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

t = Temperature(0)
print(t.fahrenheit)  # 32.0

t.fahrenheit = 212
print(t.celsius)     # 100.0

#exercise 2
"""this part was written by me but i couldn't complete these two points as i was confused
- supports getting and setting both celsius and fahrenheit (updating the internal Kelvin consistently)
- validates values so temperature can never be set below absolute zero (0 K)"""

class Thermostat:
    def __init__(self,kelvin):
        self._kelvin = kelvin
    
    @property
    def kelvin(self):
        return self._kelvin
    
    @property
    def celsius(self):
        return self.kelvin - 273.15
    
    @celsius.setter
    def celsius(self,value):
        return (value + 273.15)
    
    @property
    def fahrenheit(self):
        return (self.kelvin * 9/5 - 459.67)
    
    @fahrenheit.setter
    def fahrenheit(self,value1):
        return (value1 + 459.67 * 5/9)

t = Thermostat(273.15)   # 0 °C
print(t.celsius)         # 0.0
print(t.fahrenheit)      # 32.0

t.fahrenheit = 212
print(t.celsius)         # 100.0
print(t.kelvin)          # 373.15

# with these two points added this code i got this from AI
class TemperatureError(ValueError):
    pass

class Thermostat:
    def __init__(self, kelvin):
        self._set_kelvin(kelvin)

    # --- internal helper
    def _set_kelvin(self, k):
        if not isinstance(k, (int, float)):
            raise TypeError("temperature must be a number")
        if k < 0:
            raise TemperatureError("temperature cannot be below absolute zero (0 K)")
        self._kelvin = float(k)

    # --- kelvin property (read-only)
    @property
    def kelvin(self):
        return self._kelvin

    # --- celsius property
    @property
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("celsius must be a number")
        k = float(value) + 273.15
        self._set_kelvin(k)

    # --- fahrenheit property
    @property
    def fahrenheit(self):
        return (self._kelvin - 273.15) * 9.0/5.0 + 32.0

    @fahrenheit.setter
    def fahrenheit(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("fahrenheit must be a number")
        c = (float(value) - 32.0) * 5.0/9.0
        k = c + 273.15
        self._set_kelvin(k)

    def __repr__(self):
        return f"Thermostat(kelvin={self._kelvin:.5f})"

#exercise 3
class Even_Or_Odd:
    def __init__(self,num):
        self.num = num
    
    def even_or_odd(self):
        if self.num % 2 == 0:
            print("the number is even")
        else:
            print("the number is odd")

n1 = Even_Or_Odd(4)
n1.even_or_odd()   # the number is even

n2 = Even_Or_Odd(5)
n2.even_or_odd()   # the number is odd

#exercise 4
class EvenOrOdd:
    def __init__(self, num):
        if not isinstance(num, int):
            raise TypeError("num must be an int")
        self.num = num

    def is_even(self):
        return self.num % 2 == 0

    def __str__(self):
        return "the number is even" if self.is_even() else "the number is odd"

    @classmethod
    def from_string(cls, s):
        """
        Create an instance from a string.
        Accepted simple formats:
          - "42"
          - "num:42" or "num: 42"
          - "even 42" or "odd 42" (prefix "even"/"odd" ignored, numeric part used)
        Raises ValueError on malformed input or non-integer values.
        """
        if not isinstance(s, str):
            raise TypeError("input must be a string")

        token = s.strip()

        # remove common prefix forms
        for prefix in ("num:", "num", "even", "odd"):
            if token.lower().startswith(prefix):
                token = token[len(prefix):].strip()
                break

        if not token:
            raise ValueError("no numeric value found in input")

        # allow integers only
        try:
            value = int(token)
        except ValueError:
            raise ValueError(f"invalid integer value: {token!r}")

        return cls(value)

#exercise 5
class EvenOrOdd:
    def __init__(self, num):
        self.num = num

    def is_even(self):
        return self.num % 2 == 0

    def print_data(self):
        """Prints a short summary about the object."""
        kind = "even" if self.is_even() else "odd"
        print(f"number: {self.num} — {kind}")

# Example usage
n1 = EvenOrOdd(4)
n1.print_data()   # prints: number: 4 — even

n2 = EvenOrOdd(5)
n2.print_data()   # prints: number: 5 — odd

#exercise 6
import functools

def repeat(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Example
@repeat(3)
def hello():
    print("Hi")

hello()  # prints "Hi" three times