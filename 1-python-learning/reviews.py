import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    result = ""

    for i in range(0,n):
        act = input()
        j = 0
        result_even = list()
        result_odd = list()
        while j < len(act):
            
            if(j%2==0):
                result_even.append(act[j])
            else:
                result_odd.append(act[j])
            j += 1
    result.join(result_even)
    result += " "
    result.join(result_odd)


print(result_even)
