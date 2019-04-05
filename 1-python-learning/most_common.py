#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict
from collections import Counter


if __name__ == '__main__':

    chars = OrderedDict()
    s = input()
    
    for i in s:
        chars[i] = chars.get(i,0) + 1
    
    sorted(chars, key=chars.get, reverse=True)
    
    ##for j,k in chars.items():
      ##  print(j,k)
    #for i in high:
       # print(i[0],i[1])
