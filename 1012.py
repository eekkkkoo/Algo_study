# 런타임 에러 발생 방지
import sys
sys.setrecursionlimit(10**6)
# 입력
T = int(input())
M, N, K = [0] * T, [0] * T, [0] * T
graph = [[] for _ in range(T)]
for i in range(T):
    M[i], N[i], K[i] = map(int,input().split())
    for _ in range(K[i]):
        x, y = map(int, input().split())
        graph[i].append((x, y))
# 함수
def DFS(graph, x, y, num):
    if (x, y) not in graph[num]:
        return
    graph[num].remove((x, y))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if (X, Y) in graph[num]:
            DFS(graph, X, Y, num)
# 출력
for i in range(T):
    number = 0
    while graph[i]:
        x, y = graph[i][0]
        DFS(graph, x, y, i)
        number += 1
    print(number)