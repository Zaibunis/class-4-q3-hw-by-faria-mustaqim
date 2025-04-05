##Working with Dates in Python
#Use the datetime module for handling dates and times. Here's an example:


from datetime import date
today = date.today()  # Get today's date
print("Today's date:", today)

#Formatting Dates
#You can format date and time in various ways using the strftime() method:

import datetime

# Get the current date and time
now = datetime.datetime.now()

print(now)  
print(now.date())  
