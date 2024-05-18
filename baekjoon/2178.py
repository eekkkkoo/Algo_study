# 입력
N, M = map(int, input().split())
graph = [0] * N
for i in range(N):
    graph[i] = list(map(int, input()))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# BFS함수
def BFS(graph, x, y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < N and 0<= Y < M:
                if graph[X][Y] == 1:
                    graph[X][Y] = graph[x][y] + 1
                    queue.append((X, Y))
# 출력
BFS(graph, 0, 0)
print(graph[N-1][M-1])
