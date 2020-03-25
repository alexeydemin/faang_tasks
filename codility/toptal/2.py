def solution(X, Y):
    dic = {}
    for i in range(len(X)):
        b = simplisize(X[i], Y[i])
        print(b)
        inx = str(b[0]) + '/' + str(b[1])
        if inx in dic:
            dic[inx] += 1
        else:
            dic[inx] = 1
    return max(dic.values())


def simplisize(x, y):
    if x == 0:
        return (0, 0)
    for i in range(round(min(x, y)), 1, -1):
        if x % i == y % i == 0:
            x = x // i
            y = y // i
    return (x, y)


# print(solution([1, 2, 3, 4, 0], [2, 3, 6, 8, 4]))
#print(solution([3, 3, 4, 0, 0], [5, 4, 3, 5, 6]))
print(solution([3, 3, 4, 5, 10], [5, 4, 3, 1, 2]))
# print(solution([4,4,7,1, 2], [4,4,8,1,2]))
# print(solution([1,2,3,1, 2], [2,4,6,5,10]))
# simplisize(3, 6)
