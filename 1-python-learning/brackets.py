def checkio(expression):
    curly_bracket   = 0
    squared_bracket = 0
    angle_bracket   = 0
    brackets        = ""
    open_curly      = True
    close_curly     = True
    open_squared    = True
    close_squared   = True
    open_angle      = True
    close_angle     = True
    
    for i in expression:
        if(i == '('):
            curly_bracket += 1
        if(i == ')'):
            curly_bracket -= 1
        if(i == '{'):
            angle_bracket += 1
        if(i == '}'):
            angle_bracket -= 1
        if(i == '['):
            squared_bracket += 1
        if(i == ']'):
            squared_bracket -= 1

    for i in expression:
        if (i == '(' or i == ')' or i == '[' or i == ']' or i == '{' or i == '}'):
            brackets += i


    for i in brackets:
        if(i == '('): open_curly = False
        if(i == '['): open_squared = False
        if(i == '{'): open_angle = False
        
        if(i == ')'):
            if(open_angle == False or open_squared == False): return False
        if(i == ']'):
            if(open_curly == False or open_angle == False):   return False
        if(i == '}'):
            if(open_curly == False or open_squared == False): return False
    
    
    if(curly_bracket == 0 and squared_bracket == 0 and angle_bracket == 0):
        return True
    else:
        return False
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("((5+3)*2+1)"))
