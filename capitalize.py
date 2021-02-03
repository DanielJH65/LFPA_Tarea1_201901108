import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    lista= s.split(" ")
    lista = " ".join(i.capitalize() for i in lista)
        
    return lista

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()