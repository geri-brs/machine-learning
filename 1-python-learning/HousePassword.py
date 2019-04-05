data = "QwErTy911poqqqq"
upper = 0
lower = 0
digit = 0
chlen = len(data)

for i in data:
    if (i.isupper()): upper = upper + 1
    if (i.islower()): lower = lower + 1
    if (i.isdigit()): digit = digit + 1

if (chlen>=10 and lower>=1 and upper>=1 and digit>=1): print("True")
else: 
    print("Else")    

