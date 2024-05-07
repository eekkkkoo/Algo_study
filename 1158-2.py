# baekjoon 1158
import sys

n, k = map(int, sys.stdin.readline().split())
data = list(range(1, n+1))
result = []
i=0
while data:
    i = (i+k-1)%len(data)
    result.append(str(data.pop(i)))

print(f'<{", ".join(result)}>')