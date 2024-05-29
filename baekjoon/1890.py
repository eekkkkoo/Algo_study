n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
result = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] > 0 and graph[i][j] > 0:
            a = graph[i][j]
            if i + a < n:
                dp[i+a][j] += dp[i][j]
            if j + a < n:
                dp[i][j+a] += dp[i][j]
print(dp[n-1][n-1])