import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

left = 1
right = max(lst)

while left <= right:
    mid = (left + right) // 2
    sum = 0
    for i in lst:
        if i > mid:
            sum += i - mid
    if sum >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)
