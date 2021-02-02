import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2 == 0:
        if n>5 and n<21:
            print('Weird')
        else:
            print('Not Weird')
    else:
        print('Weird')