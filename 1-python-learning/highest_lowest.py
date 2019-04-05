def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

if __name__ == '__main__':
        print(high_and_low("2004 1508 1957 304 95 1611 1964 1504 3141 1856 2819 1880 930 2031 253 1603 2124 972 2871 2489 1852 2983"))
