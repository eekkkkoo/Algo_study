import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))
lst.sort(key=lambda x: (x[1], x[0]))
count = 1
start = lst[0][1]
for i in range(1, N):
    if start <= lst[i][0]:
        start = lst[i][1]
        count += 1
print(count)