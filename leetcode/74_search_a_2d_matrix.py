from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for line_num, line in enumerate(matrix):
            if target < line[-1]:
                return self.searchLine(self, line, target)

    def searchLine(self, line, target):
        for l in line:
            if l == target:
                return True
        return False


print(Solution.searchMatrix(Solution, matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))   # true
print(Solution.searchMatrix(Solution, matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))  # false
