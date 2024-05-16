n = int(input())
graph = [0] * n
for i in range(n):
    graph[i] = list(map(int, input()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(graph, x, y):
    queue = [(x, y)]
    graph[x][y] = 0
    num = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < len(graph) and 0 <= Y < len(graph):
                if graph[X][Y] == 1:
                    queue.append((X, Y))
                    graph[X][Y] = 0
                    num += 1
    return num

number = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            number.append(bfs(graph, x, y))
number.sort()
print(len(number))
for i in number:
    print(i)
