class Solution:
    def maximalSquare(self, matrix):
        max_square = 0
        for j, line in enumerate(matrix):
            for i, el in enumerate(matrix[j]):
                if matrix[j][i] == '1':
                    #print(i, j)
                    max_square = max(Solution.checkMatrix(self, i, j, matrix), max_square)
        return max_square * max_square

    def checkMatrix(self, x, y, matrix):
        max_square = 1
        _x = len(matrix[0])
        _y = len(matrix)
        print(min(_x - x, _y - y))
        for length in range(1, min(_x - x, _y - y)):
            print('L=' + str(length))
            print('---')
            is_square = 1
            for i in range(0, length):
                # print(i + x, length + y, matrix[length + y][i + x])
                is_square *= int(matrix[length + y][i + x])
            # print('----')
            for i in range(0, length + 1):
                # print(length + x, i + y, matrix[i + y][length + x])
                is_square *= int(matrix[i + y][length + x])
            # print('=================')
            if is_square:
                max_square = length + 1
            else:
                return max_square
        return max_square


arr = [
    # 0    1    2    3
    ["0", "0", "0", "1"],  # 0
    ["1", "1", "1", "1"],  # 1
    ["1", "1", "1", "1"],  # 2
    ["1", "1", "1", "1"],  # 3
    ["1", "1", "0", "1"]  # 4
]
arr2 = [
    # 0    1    2    3
    ["1", "2", "3", "4"],  # 0
    ["5", "6", "7", "8"],  # 1
    ["9", "1", "2", "3"],  # 2
    ["4", "5", "6", "7"],  # 3
    ["8", "9", "1", "0"],  # 4
]

a = Solution.maximalSquare(None, arr)
# a = Solution.checkMatrix(None, 0, 1, arr)
# print(a)
