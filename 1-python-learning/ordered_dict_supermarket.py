from collections import OrderedDict

if __name__ == '__main__':
    items_num = int(input())
    dict_items = OrderedDict()
    i=0
    while i < items_num:
        item, space, amount = input().rpartition(' ')
        dict_items[item] = dict_items.get(item, 0) + int(amount)
        i+=1

    for k,v in dict_items.items():
        print(k,v)
