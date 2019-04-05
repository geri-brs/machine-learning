def sun_angle(time):
    #replace this for solution
    hh_ss = time.split(":")
    hour = int(hh_ss[0])
    minute = int(hh_ss[1])
    
    if (hour < 6): return "I don't see the sun!"
    if (hour > 12): return "I don't see the sun!"
    else:
        return ((hour-6)*15)+(minute*0.25)

if __name__ == '__main__':
    print(sun_angle("12:15"))
