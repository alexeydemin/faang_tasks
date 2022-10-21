from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        up, left = 0, 0
        right = cols - 1
        down = rows - 1
        res = []
        while len(res) < rows * cols:
            for col in range(left, right + 1):
                res.append(matrix[up][col])  # first line

            for row in range(up + 1, down + 1):
                res.append(matrix[row][right])
            if up < down:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])
            if left < right:
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        return res


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(Solution.spiralOrder(None, matrix))
# [1,2,3,6,9,8,7,4,5]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(Solution.spiralOrder(None, matrix))
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
