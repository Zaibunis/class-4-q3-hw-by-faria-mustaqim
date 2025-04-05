#What is Epoch?
#An epoch is a fixed point in time from which the system starts measuring time. In most systems, January 1, 1970, 00:00:00 (UTC) is used as the epoch.

#In simple terms, the epoch serves as the "starting point" or "zero" for timekeeping.

#Why is there an epoch?
#Consistent Timekeeping: The epoch provides a standard starting point that allows all systems to agree on the measurement of time.
#Simplified Calculations: By counting the number of seconds that have passed since the epoch, you can easily represent and compare times without worrying about complex date formats.

#time.time(): Returns the current time in seconds since the epoch as a floating-point number.

import time
current_time = time.time()
print(current_time)  

#time.localtime(seconds): Converts seconds since the epoch into a time tuple based on local time

local_time = time.localtime(current_time)
print(local_time)

#time.asctime(): Converts a time tuple into a readable string.

readable_time = time.asctime(local_time)
print(readable_time)