def solution(n):
    if n == 0:
        return [1]
    else:
        return pascal([1], n)


def pascal(arr, n):
    ret = [1]
    for i in range(len(arr)):
        if i + 1 < len(arr):
            ret.append(arr[i] + arr[i + 1])
    ret.append(1)
    return pascal(ret, n - 1) if n > 1 else ret


print(solution(5))
