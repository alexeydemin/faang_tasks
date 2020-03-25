# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A) + 1
    norm_sum = n * (n + 1) // 2
    return norm_sum - sum(A)


print(solution([]))
