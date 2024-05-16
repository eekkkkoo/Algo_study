
def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True
    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in graph:
    i.sort()

visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)
