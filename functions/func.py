#Understanding Functions in Python
#A function in Python is a reusable block of code that performs a specific task. It helps break down complex problems into smaller, more manageable pieces, making your code cleaner, modular, and easier to maintain.

def motivate():
    print("Keep up the good work!")
    print("Stay focused and make progress.")

motivate()

#Types of Functions in Python
#Built-in Functions
#These are pre-defined functions in Python. Examples include:
#print()
#len()
#sum()

print(len(["faria",4,7]))
print(sum([8,9]))

#Functions from Built-in Modules
#These are functions provided by Python modules, which need to be imported first.

import math
print(math.sqrt(5))

#User-defined Functions
#You can create your own functions to perform specific tasks.

def motivate(name):
    print("Stay focused and make progress " + name + "!")
motivate("Faria")

#Function Syntax
#Here's the basic structure for defining a function:

def sub(a,b):
    return a - b
result = sub(5,4)
print(result)

#Function Arguments
#Positional Arguments: These are the arguments passed in the order they are defined.

def greet(name, grade):
    print(f"Assalam-o-Alaikum {name}! Grade: {grade}")

greet(name="Faria", grade="9")

#Keyword Arguments: These arguments are passed by name.

def greet(name, grade):
    print(f"Assalam-o-Alaikum {name}! Grade: {grade}")

greet(name="Faria", grade="9")


#Default Arguments: These arguments have default values. If they are not provided, their default values will be used.

def motivate(name, age="15"):
    print("Stay focused and make progress " + name + "! "  + "You are " + age + " years old.")
motivate("Faria")

