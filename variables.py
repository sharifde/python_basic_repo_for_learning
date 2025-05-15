# variables.py
# This script demonstrates the use of variables in Python

# --------- Basic Variable Assignments ---------

# Integer
age = 25
print("Age:", age)

# Float
height = 5.9
print("Height:", height)

# String
name = "Sharif"
print("Name:", name)

# Boolean
is_student = True
print("Is student:", is_student)

# --------- Multiple Assignment ---------

# Assigning multiple variables in one line
x, y, z = 10, 20, 30
print("x:", x, "y:", y, "z:", z)

# Assigning the same value to multiple variables
a = b = c = 100
print("a:", a, "b:", b, "c:", c)

# --------- Data Types ---------

# List
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Tuple (immutable list)
dimensions = (1920, 1080)
print("Dimensions:", dimensions)

# Dictionary
person = {
    "name": "Sharif",
    "age": 25,
    "is_student": True
}
print("Person dictionary:", person)

# Set (unordered, unique items)
unique_numbers = {1, 2, 3, 3, 4}
print("Unique numbers:", unique_numbers)

# --------- Type Checking ---------

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of fruits:", type(fruits))

# --------- Type Casting ---------

# Convert integer to string
age_str = str(age)
print("Age as string:", age_str, "| Type:", type(age_str))

# Convert string to integer
num_str = "50"
num_int = int(num_str)
print("String to int:", num_int, "| Type:", type(num_int))

# Convert integer to float
num_float = float(age)
print("Integer to float:", num_float)

# --------- Constants (by convention) ---------

# Python does not have true constants, but all-uppercase variable names are used by convention
PI = 3.14159
GRAVITY = 9.8
print("PI:", PI)
print("Gravity:", GRAVITY)
