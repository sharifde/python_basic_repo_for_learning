# demo_functions.py
# This script demonstrates how to define and use functions in Python

# --------- 1. Basic Function ---------
# Use case: Print a simple message

def greet():
    print("Hello, welcome to Python functions!")

# Call the function
greet()


# --------- 2. Function with Parameters ---------
# Use case: Greet a user by name

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Sharif")


# --------- 3. Function with Return Value ---------
# Use case: Add two numbers and return the result

def add(a, b):
    return a + b

result = add(10, 5)
print("Sum:", result)


# --------- 4. Default Parameter ---------
# Use case: Handle optional arguments

def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Ali")


# --------- 5. Keyword Arguments ---------
# Use case: Make function calls clearer

def introduce(name, age):
    print(f"My name is {name}, and I am {age} years old.")

introduce(age=25, name="Sara")


# --------- 6. Variable Number of Arguments ---------
# Use case: Sum an unknown number of inputs

def sum_all(*numbers):
    total = sum(numbers)
    print("Sum of all numbers:", total)

sum_all(1, 2, 3)
sum_all(10, 20, 30, 40)


# --------- 7. Function with Dictionary Arguments ---------
# Use case: Accept key-value pairs as input

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Sharif", age=25, country="Pakistan")


# --------- 8. Nested Functions ---------
# Use case: Organize helper logic within another function

def outer_function(x):
    def inner_function(y):
        return y * y
    return inner_function(x)

print("Result from nested function:", outer_function(4))


# --------- 9. Lambda Function ---------
# Use case: Short, anonymous functions

square = lambda x: x * x
print("Square using lambda:", square(5))


# --------- 10. Docstrings ---------
# Use case: Describe what the function does (used by help())

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

print("Multiplication:", multiply(4, 3))
print("Function docstring:", multiply.__doc__)
