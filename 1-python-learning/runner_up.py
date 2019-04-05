if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist = list(map(int,arr))

    mylist.sort()
    unique_list = list()
    for i in mylist:
        if i not in unique_list:
            unique_list.append(i)
    unique_list.sort()
    unique_list.remove(max(unique_list))
    print(max(unique_list))
    
    

    


