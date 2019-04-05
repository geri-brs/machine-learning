def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    counter = 0
    for k,v in enumerate(text):
        if (v == symbol): counter = counter + 1
        if (counter == 2): break
    
    return k


if __name__ == '__main__':
    print('Example:')
   # print(second_index("sims", "s"))
    print(second_index("hi", " "))
