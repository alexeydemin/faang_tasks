def solution(N, K):
    cnt = 0
    while N >= 2:
        if N % 2 == 0 and K:
            N //= 2
            K-=1
        else:
            N -= 1
        cnt += 1
    return cnt


print(solution(8, 0))  # 7
print(solution(18, 2))  # 6
print(solution(10, 10))  # 4
print(solution(4, 0))  # 3
print(solution(4, 8))  # 2
print(solution(1, 8))  # 2

print(solution(6, 8))  # 3
print(solution(7, 8))  # 4

print(solution(14, 1))  # 7

