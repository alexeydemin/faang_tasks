import math
import time

def solution(X, Y):
    dic = {}
    for i in range(len(X)):
        b = simplisize(X[i], Y[i])
        # print(b)
        inx = str(b[0]) + '/' + str(b[1])
        if inx in dic:
            dic[inx] += 1
        else:
            dic[inx] = 1
    return max(dic.values())


def simplisize(x, y):
    g = math.gcd(x,y)
    x = x // g
    y = y // g
    return (x, y)


test_arrays = [
    # [[6, 2],
    #  [2, 1], 1],
    # [[1000000, 2 * 1000000],
    #  [999999, 2 * 999999], 2],
    # [[1, 2, 3, 4, 0],
    #  [2, 3, 6, 8, 4], 3],
    # [[3, 3, 4],
    #  [5, 4, 3], 1],
    # [[4, 4, 7, 1, 2],
    #  [4, 4, 8, 1, 2], 4],
    # [[1, 2, 3, 1, 2],
    #  [2, 4, 6, 5, 10], 3],
    # [[5, 0, 0, 0, 3],
    #  [5, 9, 100, 200, 3], 3],
    # [[5, 0, 0, 0, 3],
    #  [5, 9, 100, 200, 3], 3],
    # [[5, 5], [5, 5], 2],
    [range(1, 200000), range(2,200001), 1]
]
# print(solution([3, 3, 4, 5, 10], [5, 4, 3, 1, 2]))
# print(simplisize(3,5))
# print(solution([0,0,0,1,1], [2,2,2,2,3]))
# simplisize(3, 6)

start_time = time.time()

for ta in test_arrays:
    print(solution(ta[0], ta[1]), solution(ta[0], ta[1]) == ta[2])

print("--- %s seconds ---" % (time.time() - start_time))