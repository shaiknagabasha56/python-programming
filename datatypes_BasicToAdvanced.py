#author:Shaik Nagabasha
#Instagram:https://www.instagram.com/mirapakaaytech/
#Youtube: https://youtube.com/@mirapakaaytech?si=pC5ZmkIl6xgIyGuM
#GitHub: https://github.com/shaiknagabasha56

# =========================================
# 20 PYTHON PROGRAMS - DATA TYPES CONCEPT
# BASIC TO ADVANCED
# =========================================

# ---------- BASIC LEVEL (1-7) ----------

# 1. Checking type of an integer
print("1.")
age = 25
print(type(age))
print()

# 2. Checking type of a float
print("2.")
price = 99.99
print(type(price))
print()

# 3. Checking type of a string
print("3.")
name = "Alex"
print(type(name))
print()

# 4. Checking type of a boolean
print("4.")
is_active = True
print(type(is_active))
print()

# 5. Checking type of a list
print("5.")
fruits = ["apple", "banana", "cherry"]
print(type(fruits))
print()

# 6. Checking type of a tuple
print("6.")
coordinates = (10, 20, 30)
print(type(coordinates))
print()

# 7. Checking type of None
print("7.")
x = None
print(type(x))
print()


# ---------- INTERMEDIATE LEVEL (8-14) ----------

# 8. Checking type of a dictionary
print("8.")
person = {"name": "Alex", "age": 25}
print(type(person))
print()

# 9. Checking type of a set
print("9.")
colors = {"red", "green", "blue"}
print(type(colors))
print()

# 10. Type conversion - string to integer
print("10.")
num_str = "100"
num_int = int(num_str)
print(num_int, type(num_int))
print()

# 11. Type conversion - integer to float
print("11.")
num = 10
num_float = float(num)
print(num_float, type(num_float))
print()

# 12. Type conversion - list to tuple
print("12.")
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple, type(my_tuple))
print()

# 13. Checking ordered vs unordered (list vs set)
print("13.")
ordered_list = ["a", "b", "c"]
unordered_set = {"a", "b", "c"}
print("List (ordered):", ordered_list[0])     # accessible by index
print("Set (unordered):", unordered_set)       # no index access possible
print()

# 14. Demonstrating mutability - modifying a list
print("14.")
fruits = ["apple", "banana"]
print("Before:", fruits, id(fruits))
fruits.append("cherry")
print("After:", fruits, id(fruits))   # same memory address
print()


# ---------- ADVANCED LEVEL (15-20) ----------

# 15. Demonstrating immutability - modifying a string
print("15.")
name = "Alex"
print("Before:", name, id(name))
name = name + " Smith"
print("After:", name, id(name))   # different memory address
print()

# 16. Trying to modify a tuple (will raise an error - handled safely)
print("16.")
coordinates = (10, 20)
try:
    coordinates[0] = 99
except TypeError as e:
    print("Error:", e)
print()

# 17. Using frozenset (immutable version of set)
print("17.")
fs = frozenset({"red", "green", "blue"})
print(fs, type(fs))
try:
    fs.add("yellow")
except AttributeError as e:
    print("Error:", e)
print()

# 18. Checking hashability - mutable types can't be dictionary keys
print("18.")
try:
    my_dict = {[1, 2, 3]: "value"}   # list as key - will fail
except TypeError as e:
    print("Error:", e)
my_dict2 = {(1, 2, 3): "value"}      # tuple as key - works fine
print("Tuple as key works:", my_dict2)
print()

# 19. User-defined data type using a class
print("19.")
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

my_car = Car("Toyota", 180)
print(type(my_car))
print(f"Brand: {my_car.brand}, Speed: {my_car.speed}")
print()

# 20. User-defined data type using Enum
print("20.")
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED, type(Color.RED))
print(Color.GREEN.name, Color.GREEN.value)