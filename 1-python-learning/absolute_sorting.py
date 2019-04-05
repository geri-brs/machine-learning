def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

def sorting(tup):
    abs_list = []
    for i in(tup):
        abs_list.append(absolute(i))
    return abs_list
        
if __name__ == '__main__':
    
    a = (-20, -5, 10, 15)
    print(sorted(a, None, lambda a: abs(a))
