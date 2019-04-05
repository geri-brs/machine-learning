from collections import deque
import collections

if __name__ == '__main__':
    
    d = collections.deque()
    lines = int(input())
    i=0

    while i < lines:
        command = input().split(' ')
        if(command[0]=='append'): d.append(int(command[1]))
        if(command[0]=='appendleft'): d.appendleft(int(command[1]))
        if(command[0]=='pop'): d.pop()
        if(command[0]=='popleft'): d.popleft()
        if(command[0]=='extend'): d.extend(int(command[1]))
        if(command[0]=='extendleft'): d.extendleft(int(command[1]))
        if(command[0]=='clear'): d.clear()
        if(command[0]=='remove'): d.remove(int(command[1]))
        if(command[0]=='reverse'): d.reverse()
        if(command[0]=='rotate'): d.rotate(int(command[1]))
        if(command[0]=='count'): d.count(int(command[1]))
        i+=1
    
    for i in d:
        print(i,end=' ')
