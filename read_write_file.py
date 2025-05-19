# read_write_file.py
# This script demonstrates basic file input/output operations in Python

# --------- 1. Writing to a File ---------
# Use case: Save some data to a file

with open('sample.txt' ,'w') as file :
     file.write('Hello, this is the first line.\n')
     file.write("This is the second line.\n")
print('Data written to sample.txt')    

# --------- 2. Reading from a File ---------
# Use case: Read entire content of a file
with open('sample.txt' ,'r') as file :
     content =file.read()
     print("\n--- File Content (read all at once) ---")
     print(content)

# --------- 3. Reading Line by Line ---------
# Use case: Process each line individually (e.g., logs, CSV)
with open("sample.txt", "r") as file:
    print("\n--- File Content (line by line) ---")
    for line in file:
        print(line.strip())  # .strip() removes newline characters

# --------- 4. Appending to a File ---------
# Use case: Add more content without deleting existing data 
with open('sample.txt' ,'a') as file :
      file.write("This line was added later.\n")
print("\nAppended a new line to sample.txt")

# --------- 5. Reading After Append ---------

with open("sample.txt", "r") as file:
    print("\n--- File Content (after appending) ---")
    print(file.read())

# --------- 6. Handling File Not Found Error ---------
# Use case: Avoid crashing when the file doesn't exist    

try :
     with open("nonexistent.txt", "r") as file:
        print(file.read())
        
except FileNotFoundError:
     print("\nError: 'nonexistent.txt' not found.")     
       
