class Solution:
    def largestMatrix(self, ar):
        max_current = 0
        max_sq = 0
        for y, line in enumerate(ar):
            #print('===line ' + str(y) + ' ===')
            for x, el in enumerate(line):
                if el > 0:
                    max_current += 1
                    #print('max_current=' + str(max_current))
                    if Solution.isSquare(self, ar, x - max_current + 1, y, max_current):
                        max_sq = max(max_sq, max_current)
                else:
                    max_current = 0
            max_current = 0

        return max_sq

    def isSquare(self, ar, x, y, le):
        if le == 1:
            return True
        #print('> Checking if it is square: element(' + str(x) + ',' + str(y) + ')=' + str(ar[x][y]) + '; length=' + str(le))
        res = 1
        for i in range(y, y + le):
            if y + le > len(arr):
                return False
            for j in range(x, x + le):
                if x + le > len(arr[i]):
                    return False
                #print('  element(' + str(j) + ',' + str(i) + ')=' + str(ar[i][j]))
                res *= int(ar[i][j])
        #print('  is_square=' + str(res))
        return bool(res)


arr1 = [
    # 0  1  2  3
    [1, 1, 1, 1],  # 0
    [1, 1, 1, 1],  # 1
    [1, 1, 1, 1],  # 2
    [1, 0, 1, 1],  # 3
]
# arr = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]

arr = [
   # 0  1  2  3
    [1, 0, 1, 0, 0],   # 0
    [1, 0, 1, 5, 1],   # 1
    [1, 1, 1, 1, 1],   # 2
    [1, 0, 1, 1, 0]    # 3
]
a = Solution.largestMatrix(None, arr)

#print('==========================')
#print(a)

# arr = [
#     [1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1],
# ]
