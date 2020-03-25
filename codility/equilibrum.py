def solution(A):
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)
    for index in range(1, len(A) - 1):
        head += A[index]
        tail -= A[index]
        if abs(head - tail) < min_dif:
            min_dif = abs(head - tail)
    return min_dif


print(solution([-3, -1, -2, -4, -3, 0]))
#print(solution([1, 1]))
