 
aList01 = ['auto', 'villamos', 'metro']
aList02 = [i.upper() for i in aList01]

bList01 = ['aladar', 'bela', 'cecil']
bList02 = [i.title() for i in bList01]

cList01 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cList02 = [0 for i in range(10)]

dList01 = "1234567"
dList02 = [int(i) for i in dList01]

eList01 = "The quick brown fox jumps over the lazy dog"
eList02 = [len(i) for i in eList01.split()]


print(eList02)
