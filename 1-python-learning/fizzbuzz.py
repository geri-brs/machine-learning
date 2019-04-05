# Your optional code here
# You can import some modules or create additional functions


def checkio(number: int) -> str:
    
    result = ""
    if ((number % 3 == 0) and (number % 5 == 0)):
        result = str(number) + " is divisible by 3 and 5"
    if (number % 3 == 0):
        result = str(number) + " is divisible by 3"
    if (number % 5 == 0):
        result = str(number) + " is divisible by 5"
    if (not((number % 3 == 0) and (number % 5 == 0))):
        result = str(number) + " is not divisible by 3 or 5"
    return result


if __name__ == '__main__':
    print(checkio(8))
