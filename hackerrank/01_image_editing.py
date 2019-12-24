class Solution:
    def largestMatrix(self, ar):
        max_current = 0
        max_sq = 0
        for y, line in enumerate(ar):
            # print(y, line)
            for x, el in enumerate(line):
                if el > 0:
                    max_current += 1
                    print('max_current=' + str(max_current))
                    if Solution.isSquare(self, ar, x - max_current + 1, y, max_current):
                        max_sq = max(max_sq, max_current)
                else:
                    max_current = 0
            max_current = 0
            print('===line ' + str(y+1) +' ===')
        return max_sq

    def isSquare(self, ar, x, y, le):
        if le == 1:
            return True
        print(x, y, le)
        res = 1
        for i in range(x, x + le):
            for j in range(y, y + le):
                if y + le > len(arr[i]):
                    return False
                print('---i=' + str(i) + ';j=' + str(j) + ';a=' + str(ar[i][j]) + ';---')
                res *= ar[i][j]
        print(str(le) + 'is_square=' + str(res))
        return bool(res)


arr = [
    # 0  1  2  3
    [1, 1, 1, 1],  # 0
    [1, 1, 1, 1],  # 1
    [1, 1, 1, 1],  # 2
    [1, 0, 1, 1],  # 3
]
a = Solution.largestMatrix(None, arr)

print('==========================')
print(a)

# arr = [
#     [1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1],
# ]
