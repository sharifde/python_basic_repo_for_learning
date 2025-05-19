# conditionals.py
# This script demonstrates conditional statements in Python

# --------- 1. Basic if Statement ---------
# Use case: Check if a number is positive

number = 10
if number > 0:
    print("The number is positive.")

# --------- 2. if-else Statement ---------
# Use case: Decide between two conditions

age = 17
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# --------- 3. if-elif-else Statement ---------
# Use case: Check multiple conditions in sequence

marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

# --------- 4. Nested if Statements ---------
# Use case: Multiple levels of decision-making

username = "sharif"
password = "1234"

if username == "sharif":
    if password == "1234":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

# --------- 5. Logical Operators ---------
# Use case: Combine multiple conditions

has_ticket = True
is_sober = True

if has_ticket and is_sober:
    print("You can enter the concert.")
else:
    print("Entry denied.")

# --------- 6. Ternary Operator ---------
# Use case: One-line if-else

x = 10
result = "Even" if x % 2 == 0 else "Odd"
print("x is", result)

# --------- 7. Checking Truthy/Falsy Values ---------

value = ""

if value:
    print("This has some content.")
else:
    print("This is empty or False.")
