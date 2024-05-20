import sys

N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.append(0)
time.sort()
for i in range(1, N+1):
    time[i] += time[i-1]
result = 0
for t in time:
    result += t
print(result)