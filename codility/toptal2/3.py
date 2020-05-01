import statistics


def solution(A, S):
    l = len(A)
    cnt = 0
    for s in range(l):
        for e in range(1, l + 1):
            if s < e:
                #print(s, e, A[s:e], statistics.mean(A[s:e]))
                if statistics.mean(A[s:e]) == S:
                    cnt += 1
    return cnt


print(solution([2, 1, 3], 2))  # 3
print(solution([0, 4, 3, -1], 2))  # 2
print(solution([2, 1, 4], 3))  # 0

print(solution([3], 3))  # 0
