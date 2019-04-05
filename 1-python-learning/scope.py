import numpy as np
if __name__ == '__main__':

    readed = input()
    numbers = np.fromstring(readed, dtype=int, sep=' ')
    max = 0
    
    i = 0
    while i < (len(numbers)-1):
        j = 0
        while j < (len(numbers)):
            if(np.absolute(numbers[i]-numbers[j]) > max):
                max = np.absolute(numbers[i]-numbers[j])
            j += 1
        i += 1
    
    print(max)
