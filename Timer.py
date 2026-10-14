# vs code auto completion method
import time

my_time = int(input("Enter the time in seconds: "))

for i in range(my_time, 0, -1):
    mins, secs = divmod(i, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)

print("\a Time's up!")

""" This is my own method of coding the same timer """
"""import time

my_time = int(input("Enter the time in seconds: "))

for i in range(my_time, 0, -1):
    sec= i%60
    mins= i//60
    hrs= (i//3600 ) 
    print(f"{hrs:02}:{mins:02}:{sec:02}")
    time.sleep(1)

print("Time's up!")"""

""" Vs Code is lowkey spoiling my coding skills """