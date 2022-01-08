# imports
import os
from rich import print
import time
from random import seed
from random import randint

# color class

# seed random number generator
seed(1000)

# main
loop = True

while loop == True:
    ask = int(input("Enter first number to generate (type 'q' to quit): "))
    ask2 = int(input('Enter second number to generate: '))
    value = randint(ask, ask2)
    print(value)
    time.sleep(1)
    if ask == 'q':
        loop == False
    else:
        loop == True
