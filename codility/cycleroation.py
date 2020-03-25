def solution(A, K):
    N = len(A)
    return [] if not N else A[-K % N:] + A[:-K % N]


print(solution([0], 101))
