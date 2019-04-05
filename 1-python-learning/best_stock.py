def best_stock(data):
    
    max_key = ""
    max_value = 0
    for i in (data):
        if (data[i] > max_value):
            max_key = i
            max_value = data[i]
    
    return max_key


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))
