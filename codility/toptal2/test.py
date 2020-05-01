# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    dic = {}
    mx = float('-inf')
    for a in A:
        if a > 0:
            dic[a] = True
            mx = max(mx, a)
    if mx == float('-inf'):
        return 1

    for b in range(1, mx + 2):
        if b not in dic:
            return b


A = [7,8]
print(solution(A))
