import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def DFS(start, visited):
    visited[start] = True
    for stop in graph[start]:
        if not visited[stop]:
            DFS(stop, visited)

count = 0
visited = [False] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        DFS(i, visited)
        count += 1
print(count)
