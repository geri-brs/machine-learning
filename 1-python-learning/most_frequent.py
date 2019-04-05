import numpy as np

if __name__ == '__main__':

    a = []
    for i in range(5):
        a.append(i)
    
    print(a)

    for i in(a):
        a[i] += 1
    print(a)
