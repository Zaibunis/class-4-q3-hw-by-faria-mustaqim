# Python Concepts Guide 🚀

This guide covers essential Python concepts: **Functions**, **Modules**, **Date & Time**, **Math Operations**, **Calendar**, **File Handling**, and **Exception Handling**. Each section is explained with easy-to-understand examples.

---

## 📚 **Functions**: Organize Your Code

Functions help to break down your code into reusable pieces.

### Example:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
📦 Modules: Reuse Built-in Features
Modules let you organize code into separate files, and Python comes with many useful built-in modules.

Example (Using math module):
python
Copy
Edit
import math
print(math.sqrt(16))  # Output: 4.0
🗓️ Date & Time: Handle Dates and Times with Ease
The datetime module allows you to work with dates and times easily.

Example (Getting current date and time):
python
Copy
Edit
import datetime
now = datetime.datetime.now()
print(now)  # Output: 2025-04-06 14:30:15
Example (Formatting date and time):
python
Copy
Edit
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: 2025-04-06 14:30:15
➗ Math: Perform Calculations
Python’s math module helps you perform mathematical operations like square roots, logarithms, and more.

Example (Square Root Calculation):
python
Copy
Edit
import math
print(math.sqrt(16))  # Output: 4.0
📆 Calendar: Work with Calendar
The calendar module provides functions to work with calendars.

Example (Print Calendar for a Month):
python
Copy
Edit
import calendar
print(calendar.month(2025, 1))  # Output: January 2025 calendar
📂 File Handling: Read and Write to Files
File handling in Python is easy! You can read from and write to files using built-in functions.

Example (Writing to a File):
python
Copy
Edit
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
🚨 Exception Handling: Handle Errors Gracefully
Python provides error handling using try, except, and finally.

Example (Basic Exception Handling):
python
Copy
Edit
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always run.")
Happy Coding! 🚀

yaml
Copy
Edit

---

## ✍️ **Author**

Created by [Faria Mustaqim](#)  
Leader Student, Governor Sindh Initiative for AI, Web 3.0, and Blockchain
