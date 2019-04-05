def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    osszeg = 0
    eredmeny = 0
    
    if (len(array) == 0): return 0
    
    for i in array:
        if (array.index(i) % 2 == 0):
            print(osszeg+i, " = ", osszeg, " + ", i)
            osszeg = osszeg + i
            
    eredmeny = osszeg * array[-1]

    return eredmeny

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    #print(checkio([0, 1, 2, 3, 4, 5]))
    #print(checkio([-37,-36,-19,-99,29,20,3,-7,-64,84,36,62,26,-76,55,-24,84,49,-65,41]))
    print(checkio([-37,-36,-19,-99,29,20,3,-7,-64,84]))
