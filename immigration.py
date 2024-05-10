def solution(n, times):
    left = 1
    right = max(times) * n
    time = 0
    while left <= right:
        mid = (left + right) // 2
        people = 0 
        for i in times:
            people += mid // i
        if people >= n:
            time = mid
            right = mid - 1
        elif people < n:
            left = mid + 1
    return time

if __name__ == '__main__':
    print(solution(6, [7, 10]))