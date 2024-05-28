import sys

N, S, M = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))
dp = [[False] * (M+1) for _ in range(N+1)]
dp[0][S] = True
for i in range(N):
    for j in range(M+1):
        if dp[i][j] == True:
            if 0 <= j + V[i] <= M:
                dp[i+1][j+V[i]] = True
            if 0 <= j - V[i] <= M:
                dp[i+1][j-V[i]] = True
result = -1
for i in range(M, -1, -1):
    if dp[-1][i] == True:
        result = i
        break
print(result)