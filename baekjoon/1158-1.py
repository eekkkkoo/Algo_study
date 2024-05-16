# baekjoon 1158
import sys

command = list(map(int, sys.stdin.readline().split()))
data = list(range(1, command[0]+1))
q = []
result = []
i=0
while data:
    q.append(data[0])
    data.pop(0)
    data.append(q[-1])
    if i % (command[1]-1) != 0 or len(data) == 1:
        result.append(data[0])
        data.pop(0)
    i+=1

print('<', ", ".join([f'{a}' for a in result]), '>', sep='')
