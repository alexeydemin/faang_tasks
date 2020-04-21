from typing import List


class Solution:
    def __init__(self):
        self.min = float('inf')
        self.n = 0
        self.m = 0
        self.grid = []

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        if not self.m:
            return 0
        self.n = len(grid[0])

        self.step(0, 0, 0)
        return self.min

    def step(self, x, y, ln):

        ln += self.grid[y][x]

        if y == self.m - 1 and x == self.n - 1:
            if ln < self.min:
                self.min = ln
            ln = 0

        if x < self.n - 1:
            self.step(x + 1, y, ln)

        if y < self.m - 1:
            self.step(x, y + 1, ln)


s = Solution()

grid = [
    [1, 3, 1],
    [1, 1, 1],
    [4, 1, 1]
]

grid = [
]

print(s.minPathSum(grid))  # 7
