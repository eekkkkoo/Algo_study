N = int(input())
block = list(input())
def go(x):
    if x == 'B':
        return 'O'
    elif x == 'O':
        return 'J'
    else:
        return 'B'
i = 0
dp = [1000000] * N
dp[0] = 0
for i in range(N):
    next = go(block[i])
    for j in range(i+1, N):
        if block[j] == next:
            dp[j] = min(dp[j], dp[i]+(j-i)**2)
if dp[-1] == 1000000:
    print(-1)
else:
    print(dp[-1])