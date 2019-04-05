from collections import Counter

sizes = []
line1 = input()
line2 = input()

sizes = line2.split(' ')
size_dict = Counter(sizes)
amount = 0
n = int(input())
for j in range(0,n):
    act = input()
    act_arr = act.split(' ')
    for i in size_dict.keys():
        if (i == act_arr[0] and size_dict[i]>0):
            size_dict[i] -= 1
            amount += int(act_arr[1])

print(amount)



