import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n in range(1,5):
        if n in [2,4]:
            print ("Not weird")
        else:
            print("Weird")
    elif n in range(6,19):
        print("Weird")
    elif n >= 20:
        print("Not Weird")
    else:
        print("Please enter a number.")