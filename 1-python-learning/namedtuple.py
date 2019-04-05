from collections import namedtuple

if __name__ == '__main__':
    Student = namedtuple('Student','ID MARKS CLASS NAME')
    num_students = int(input())
    columns = input().split()
    grades = 0
    marks = ""
    i=0

    while i<len(columns):
        if(columns[i] == "MARKS"): marks = i
        i+=1

    for i in range(num_students):
        read_line = input().split()
        grades += int(read_line[marks])
    
    print(grades/num_students)
