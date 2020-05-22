from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows,cols = len(matrix),len(matrix[0])
        new = [[0 for i in range(cols)] for j in range(rows)]
        count_squre = 0
        for i in range(rows):
            for j in range(cols):
                if i==0 or j==0:
                    new[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    new[i][j] = 0
                else:
                    new[i][j] = matrix[i][j] + min(new[i-1][j],new[i-1][j-1],new[i][j-1])
                count_squre += new[i][j]
        return count_squre
print(Solution.countSquares(None, [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]))  # 15

print(Solution.countSquares(None, [
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 0]
]))  # 7