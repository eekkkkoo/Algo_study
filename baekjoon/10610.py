N = list(map(int, input()))
if sum(N)%3 == 0 and 0 in N:
    N.sort(reverse=True)
    print(''.join(map(str, N)))
else:
    print(-1)