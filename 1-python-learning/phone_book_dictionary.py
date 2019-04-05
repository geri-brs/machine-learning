if __name__ == '__main__':
    phone_book = {}

    counter = int(input())
    
    i = 0
    while  i < counter:
        person = input()
        datas = person.split(' ')
        phone_book[datas[0]] = datas[1]
        i += 1
    
    j = 0
    results = list()
    while j < counter:
        look_up = input()
        if (phone_book.get(look_up)):
            results.append(look_up + "=" + phone_book.get(look_up))
        else:
            results.append("Not found")
        j += 1
    
    for l in results:
        print(l)
