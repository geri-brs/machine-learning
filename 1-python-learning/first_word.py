import re

def first_word(str):

    if(str[0] == ' '):
        new_text = str.split()
        print('elso')
    else:
        new_text = re.split('\W+',str)
        print('masodik')
    return new_text


if __name__ == '__main__':
    print("Example:")
    print(first_word('... and so on ...'))
