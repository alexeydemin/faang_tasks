def solution(A):
    m = len(A)
    if not m:
        return 0
    n = len(A[0])
    mx = 0
    for j in range(m):
        #print(A[j])
        for i in range(n):
            #print(A[j][i])
            r = count_dir(m, n, j, i, A)
            if r > mx:
                mx = r
    return mx


def get_zeros(n):
    s = str(n)
    return len(s) - len(s.rstrip('0'))


def count_dir(m, n, j, i, A):
    c1 = count_up(m, j, i, A) * count_ri(n, j, i, A) *A[j][i]
    c2 = count_up(m, j, i, A) * count_do(m, j, i, A)  *A[j][i]
    c3 = count_up(m, j, i, A) * count_le(n, j, i, A)  *A[j][i]
    c4 = count_ri(n, j, i, A) * count_do(m, j, i, A)  *A[j][i]
    c5 = count_ri(n, j, i, A) * count_le(n, j, i, A)  *A[j][i]
    c6 = count_do(m, j, i, A) * count_le(n, j, i, A)  *A[j][i]
    return max(
        get_zeros(c1),
        get_zeros(c2),
        get_zeros(c3),
        get_zeros(c4),
        get_zeros(c5),
        get_zeros(c6)
    )


def count_up(m, j, i, A):
    r = 1
    for k in range(j):
        r *= A[k][i]
    return r


def count_do(m, j, i, A):
    r = 1
    for k in range(j+1, m):
        r *= A[k][i]
    return r

def count_le(n, j, i, A):
    r = 1
    for k in range(i):
        r *= A[j][k]
    return r


def count_ri(n, j, i, A):
    #print(n,j,i,A, list(range(i+1, n)))
    r = 1
    for k in range(i+1, n):
        r *= A[j][k]
    return r


A = [
    [6, 25, 4, 10],
    [12, 25, 1, 15],
    [7, 15, 15, 5]
]

B = [
    [5, 8, 3, 1],
    [4, 15, 12, 1],
    [6, 7, 10, 1],
    [9, 1, 2, 1]
]

B = [[1, 10],
     [100, 10],
     ]

print(solution(B))
