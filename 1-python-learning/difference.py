def checkio(number):
    
    szorzat = 1
    
    for i in str(number):
       if(int(i) != 0): szorzat = szorzat * int(i)
    
        
    return szorzat

print(checkio(52))
