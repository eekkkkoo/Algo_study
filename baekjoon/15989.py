T = int(input())
dp = [1] * 10001
for i in range(2, 10001):
    dp[i] += dp[i-2]
for i in range(3, 10001):
    dp[i] += dp[i-3]
result = [0] * T
for i in range(T):
    n = int(input())
    result[i] = dp[n]
for i in range(T):
    print(result[i])
