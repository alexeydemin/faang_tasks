class Solution:
    # this solution would not work
    def maximalSquare(self, matrix):
        max_current = 0
        max_sq = 0
        ar = matrix
        for y, line in enumerate(ar):
            print('===line ' + str(y) + ' ===')
            for x, el in enumerate(line):
                if el != '0':
                    max_current += 1
                    print('max_current=' + str(max_current))
                    if Solution.isSquare(self, ar, x - max_current + 1, y, max_current):
                        max_sq = max(max_sq, max_current)
                else:
                    max_current = 0
            max_current = 0

        return max_sq * max_sq

    def isSquare(self, ar, x, y, le):
        if le == 1:
            return True
        print('> Checking if a square: element(' + str(x) + ',' + str(y) + ')=' + str(ar[y][x]) + '; length=' + str(le))
        res = 1
        if y + le - 1 > len(ar) - 1:
            return False
        for j in range(y, y + le):
            # print(y, y + le)
            #            if x + le > len(ar):
            #                print('Y our of range. Length=' + str(len(ar)) + ';y+le=' + str(x + le))
            #                return False
            for i in range(x, x + le):
                #               if i > len(ar):
                #                   return False
                #              if y + le >= len(ar[i]):
                #                  print('X our of range')
                #                  return False
                # print('  element(' + str(i) + ',' + str(j) + ')')
                print('  element(' + str(i) + ',' + str(j) + ')=' + str(ar[j][i]))
                res *= int(ar[j][i])
        print('  is_square=' + str(res))
        return bool(res)


arr2 = [
    ["1", "2"],
    ["3", "4"]
]
arr = [
    ["0", "0", "0", "1"],
    ["1", "1", "0", "1"],
    ["1", "1", "1", "1"],
    ["0", "1", "1", "1"],
    ["0", "1", "1", "1"]
]
# arr = [
#    # 0  1  2  3
#     [1, 0, 1, 0, 0],   # 0
#     [1, 0, 1, 1, 1],   # 1
#     [1, 1, 1, 1, 1],   # 2
#     [1, 0, 1, 1, 1]    # 3
# ]
a = Solution.maximalSquare(None, arr)

print('==========================')
print(a)

# arr = [
#     [1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1],
#     [1, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1],
# ]
