if __name__ == '__main__':
    fruits = {'alma': 12, 'banan': 5, 'barack': 30,
              'meggy': 67, 'dinnye': 22, 'eper': 81}

    max = 0
    str = ''
    for i in fruits:
        if (fruits[i] > max):
            max = fruits[i]
            str = i
            
    print(str, max)
