str = "ddvvrwwwrggg"
max_len = 0
counter = 0

for i in range(0, len(str)-1):
    if (str[i] == str[i+1]): 
        counter = counter +1
        print("if  counter erteke: ", counter)
        if (counter > max_len):
            max_len = counter + 1
            print("max_len: ", max_len)
    else:
        counter = 0


print(max_len)


