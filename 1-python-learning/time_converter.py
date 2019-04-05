def time_converter(time):
    splitted = time.split(":")
    hh = int(splitted[0])
    mm = int(splitted[1][0:2])
    period = splitted[1][-4:]
    new_time = ""
    if (hh == 12 and mm == 00):
        return "00:00"
    if (period == "a.m."):
        if (hh < 10):
            new_time += "0" + str(hh)
        else:
            new_time += str(hh)
        if (mm < 10):
            new_time += ":" + "0" + str(mm)
        else:
            new_time += str(mm)
            
    if (period == "p.m."):
        if (hh < 12):
            hh += 12
            new_time += str(hh)
        else:
            new_time += str(hh)
        if (mm < 10):
            new_time += ":" + "0" + str(mm)
        else:
            new_time += ":" + str(mm)
    
    return new_time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:00 p.m.'))
