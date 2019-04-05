def find_message(str):
    sentence = str.split()
    key = ""

    for word in sentence:
        for letter in word:
            if (letter.isupper()): key += letter

    return key

    

if __name__ == '__main__':
    print(find_message("HELLO WORLD!!!"))
