# loops.py
# This script demonstrates the use of loops in Python

# --------- 1. For Loop ---------
# Use case: Iterating over a list

fruits = ["apple", "banana", "cherry"]
print("\nFor loop example (iterating over a list):")
for fruit in fruits:
    print("I like", fruit)

# Use case: Iterating over a range of numbers

print("\nFor loop with range (1 to 5):")
for i in range(1, 6):
    print("Number:", i)


# --------- 2. While Loop ---------
# Use case: Repeat an action until a condition is false

print("\nWhile loop example (counting down):")
count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1


# --------- 3. Break Statement ---------
# Use case: Exit the loop when a specific condition is met

print("\nBreak statement example (stop at banana):")
for fruit in fruits:
    if fruit == "banana":
        print("Found banana, stopping loop.")
        break
    print("Current fruit:", fruit)


# --------- 4. Continue Statement ---------
# Use case: Skip the current iteration and continue with the next one

print("\nContinue statement example (skip banana):")
for fruit in fruits:
    if fruit == "banana":
        continue
    print("Current fruit:", fruit)


# --------- 5. Nested Loops ---------
# Use case: Loop inside a loop (e.g., for matrix or grid-like structures)

print("\nNested loop example (multiplication table):")
for i in range(1, 4):  # outer loop
    for j in range(1, 4):  # inner loop
        print(f"{i} x {j} = {i * j}")
    print("----")


# --------- 6. Else with Loops ---------
# Use case: Run a block of code when the loop completes normally (no break)

print("\nFor loop with else clause:")
for number in range(1, 4):
    print("Number:", number)
else:
    print("Loop completed without break.")

# Use case: Else will NOT run if loop is exited via break

print("\nFor loop with break and else clause:")
for number in range(1, 6):
    if number == 3:
        print("Breaking at 3")
        break
    print("Number:", number)
else:
    print("Loop completed without break.")
