def solution(A):
    n = 0
    for i, a in enumerate(A):
        if A[i] - i <= 2:
            for b in A[i:]:
                if A[i] > b:
                    n += 1
        else:
            return 'Too chaotic'
    return n


            # 0  1  2  3  4  5
r = solution([2, 1, 3, 4, 6, 5])
print(r)
