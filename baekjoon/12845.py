import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

money = 0
target = max(cards)
money += (target*(n-2)) + sum(cards)
print(money)