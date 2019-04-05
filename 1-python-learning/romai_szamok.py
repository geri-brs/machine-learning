def checkio(data):
    decimal = [int(i) for i in str(data)]
    result = ""
    roman_dict = {1: ("I","X","C","M"),
                  2: ("II","XX","CC","MM"),
                  3: ("III","XXX","CCC","MMM"),
                  4: ("IV","XL","CD"),
                  5: ("V","L","D"),
                  6: ("VI","LX","DC"),
                  7: ("VII","LXX","DCC"),
                  8: ("VIII","LXXX","DCCC"),
                  9: ("IX","XC","CM"),
    }
    
    for i, item in enumerate(decimal):
        for key, value in roman_dict.items():
            if(item == key): result += value[len(decimal)-1-i]
    
    return result
    

if __name__ == '__main__':
    print(checkio(26))
