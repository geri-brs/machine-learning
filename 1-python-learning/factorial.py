import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    szorzat = 1
    for i in range(1,n+1):
        szorzat *= i
    return szorzat

if __name__ == '__main__':
    
    n = int(input())

    result = factorial(n)

    print(result)
