import sys

k, n = map(int, sys.stdin.readline().split())
line = [0] * k
for i in range(k):
    line[i] = int(sys.stdin.readline())

left = 1
right = max(line)
answer = 0

while left <= right:
    mid = (left + right) // 2
    func = 0
    for i in range(len(line)):
        func += line[i] // mid
    if func >= n:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
