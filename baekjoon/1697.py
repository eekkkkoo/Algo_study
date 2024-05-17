import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
lst = [0] * 100001

queue = deque()
queue.append(N)
while deque:
    node = queue.popleft()
    if node == K:
        print(lst[node])
        break
    for i in (node-1, node+1, 2*node):
        if 0 <= i <= 100000 and not lst[i]:
            lst[i] = lst[node] + 1
            queue.append(i)
