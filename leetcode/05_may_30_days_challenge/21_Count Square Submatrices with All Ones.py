from typing import List


class Solution:
    def countSquares(self, m: List[List[int]]) -> int:
        rows = len(m)
        cols = len(m[0])
        new = [[0 for j in range(cols)] for i in range(rows)]

        ones = 0
        s = 0
        for i in range(cols):
            s += m[0][i]
            new[0][i] = s
        ones += s

        s = 0
        for j in range(rows):
            s += m[j][0]
            new[j][0] = s
        ones += s

        for i in range(1, cols):
            for j in range(1, rows):
                ones += m[j][i]
                new[j][i] = new[j - 1][i] + new[j][i - 1] - new[j - 1][i - 1] + m[j][i]

        total = ones
        for i in range(1, cols):
            for j in range(1, rows):
                for k in range(min(rows - i-1, cols - j-1)):
                    if new[j + k][i + k]  == (k + 1) ** 2:
                        total += 1
        return total


print(Solution.countSquares(None, [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))  # 15

# print(Solution.countSquares(None, [
#     [1, 0, 1],
#     [1, 1, 0],
#     [1, 1, 0]
# ]))  # 7
