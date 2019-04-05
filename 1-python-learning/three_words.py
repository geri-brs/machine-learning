def checkio(words):
    my_list = words.split()
    
    counter = 0
    words = False
    for i in (my_list):
        if (not(i[0].isdigit())):
            counter += 1
        else:
            counter = 0
        if (counter == 3):
            return True
    
    if (counter < 3):
        return False
    
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    checkio("one two 3 four five six 7 eight 9 ten eleven 12")
    
