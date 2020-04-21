def solution(A):
    m = len(A)
    n = len(A[0])
    cnt = 0
    for j in range(m):
        for i in range(n):
            if A[j][i] != '#':
                check(A, j, i, m, n, A[j][i])
                cnt += 1
    return cnt


def check(A, j, i, m, n, previous_color):
    if previous_color != A[j][i]:
        return
    color = A[j][i]
    A[j][i] = '#'
    if 0 <= j - 1 <= m - 1:  # up
        check(A, j - 1, i, m, n, color)
    if 0 <= j + 1 <= m - 1:  # down
        check(A, j + 1, i, m, n, color)
    if 0 <= i - 1 <= n - 1:  # left
        check(A, j, i - 1, m, n, color)
    if 0 <= i + 1 <= n - 1:  # right
        check(A, j, i + 1, m, n, color)


A = [
    [5, 4, 4],
    [4, 3, 4],
    [3, 2, 4],
    [2, 2, 2],
    [3, 3, 4],
    [1, 4, 4],
    [4, 1, 1],
]

B = [
    [6,6,6,6,6,6],
    [6,1,1,1,1,6],
    [6,6,6,6,1,6],
    [6,1,1,1,1,6],
    [6,1,6,6,6,6],
    [6,1,1,1,1,6],
    [6,1,1,1,1,6]
]

C = [
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,0,1,0,1,0],
    [0,1,1,1,1,0],
    [0,1,0,0,0,0],
    [0,1,1,1,1,0],
    [0,1,1,1,1,0]
]

D = [
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,0,1,0,0,0],
    [0,1,1,1,1,0],
    [0,0,1,0,0,0],
    [0,0,1,0,0,0],
    [0,0,1,1,1,0]
]

E = [
    [0,1,0],
    [1,1,1],
    [0,1,0],
]

F = [[77]]

print(solution(A))  # 11
print(solution(B))  # 2
print(solution(C))  # 3
print(solution(D))  # 2
print(solution(E))  # 5
print(solution(F))  # 1
