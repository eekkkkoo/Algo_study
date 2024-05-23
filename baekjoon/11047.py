import sys

N, k = map(int, sys.stdin.readline().split())
coin = []
count = 0
for i in range(N):
    a = int(sys.stdin.readline())
    coin.append(a)
coin.sort(reverse=True)
for a in coin: 
    count += (k//a)
    k %= a
print(count)