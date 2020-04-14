def solution(A):
    n = len(A)
    if n == 1:
        return A[0]
    if not n:
        return 0
    A.sort()
    sum = 0
    for i in range(1, n):
        sum += A[i] * (n - i)
    return sum + (n - 1) * A[0]


print(solution([]))
# print(solution([250, 1000, 100]))
# print(solution([1, 3, 2, 4, 5]))
