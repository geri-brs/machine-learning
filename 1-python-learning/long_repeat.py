def long_repeat(line):
    counter = 0
    longest = 0

    if (line == ''): return 0
    for i in range(0, len(line)-1):
        if(line[i] == line[i+1]):
            counter += 1
            if (counter > longest):
                longest = counter
        else:
            counter = 0
                
    return longest+1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(long_repeat('sdsffffse'))
