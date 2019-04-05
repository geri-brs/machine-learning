numbers = [1,2,3,1,3]
shadow = numbers
counter = 0


shadow.sort()
for i in shadow:
    for j=i+1 in shadow:
        if (shadow[i] == shadow[j]): counter = counter + 1

print(counter)
