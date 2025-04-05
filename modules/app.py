#🧩 What is a Module in Python?
#A module is just a Python file (.py) that contains some code (functions, variables, etc.) you can reuse in other files.

#It helps keep your code neat and clean, like keeping your clothes in separate drawers!

#✅ 1. Built-in Modules (Already in Python)
#These come pre-installed. You can use them directly!

#🧪 Example: Using math module

import random

print(random.randint(6,9))

#📦 Other built-in examples: random, os, sys

#🌍 3. External Modules (Installed by pip)
#These are made by other people and you can install them.

#📦 Example: requests module to get data from websites

#pip install pandas
import pandas as pd

data = pd.Series([10,20,30,40,50])

#Other popular ones: numpy, pandas, flask

#Basic Import

import datetime

now = datetime.datetime.now()
print("Current Time:", now)

#Import with Alias
#You can give a short name:

import pandas as pd

data = pd.Series([10, 20, 30, 40, 50])
print(data)


#Import Specific Functions
#Only take what you need:

from math import factorial, ceil

print(factorial(5))  #5 = 5 × 4 × 3 × 2 × 1 = 120
print(ceil(7.2)) # ceil() – Rounds UP to the nearest whole number

# Import Everything (Not Recommended)

from math import *
print(cos(0))  # Output: 1.0 