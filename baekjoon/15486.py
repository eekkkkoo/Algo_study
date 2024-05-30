import sys

N = int(sys.stdin.readline())
day = [0] * (N+1)
for i in range(1, N+1):
    day[i] = list(map(int, sys.stdin.readline().split()))
dp = [0] * (N+1)
for i in range(1, N+1):
    a = day[i][0]
    dp[i] = max(dp[i-1], dp[i])
    if i+a-1 <= N:
        dp[i+a-1] = max(dp[i-1]+day[i][1], dp[i+a-1])
print(max(dp))