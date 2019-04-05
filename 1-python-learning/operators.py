import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    result = round(meal_cost + (meal_cost*(tip_percent/100)) + (meal_cost*(tax_percent/100)))
    return result

if __name__ == '__main__':
    meal_cost = 10.25

    tip_percent = 17

    tax_percent = 5

    print(24%2==0)
