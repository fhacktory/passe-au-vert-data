from datetime import time

x = excel_time # a float
x = int(x * 24 * 3600 * 1000) # convert to number of microseconds

my_time = time(x // (3600 * 1000), 
(x % (3600 * 1000))//(60 * 1000), 
x % (3600 * 60 * 1000),
x ) # hours, minutes, seconds
