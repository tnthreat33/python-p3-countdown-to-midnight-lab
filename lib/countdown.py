# your code goes here!
import time 

def countdown(num):
    count = num
    while count > 0:
        print(f'{count} SECOND(S)!')
        count -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(num):
    count = num
    while count > 0:
        print(f'{count} SECOND(S)!')
        count -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")