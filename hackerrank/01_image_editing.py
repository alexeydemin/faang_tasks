class Solution:
    def largestMatrix(self, ar):
        max_current = 0
        max_sq = 0
        for y, line in enumerate(ar):
            # print(y, line)
            for x, el in enumerate(line):
                if el > 0:
                    max_current += 1
                    print(max_current)
                    # if Solution.isSquare(self, ar, x, y, max_current):
                    #     max_sq = max(max_sq, max_current)
                else:
                    max_current = 0
            max_current = 0
            print('======')
        return max_sq

    def isSquare(self, ar, x, y, le):
        print(x, y, le)
        res = 1
        for i in range(x, x + le):
            for j in range(y, y + le):
                res *= arr[i][j]
        #print(res)
        return res


# arr = [
#     [1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1],
# ]
arr = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 0, 0, 1],
]
a = Solution.largestMatrix(None, arr)
#a = Solution.isSquare(None, arr, 2, 2, 3)
# print('===')
print(a)

# IV = 4
# IX = 9
# XL
# XC
# CD
# CM
#
