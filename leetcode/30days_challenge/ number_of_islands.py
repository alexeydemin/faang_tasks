from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        for j in range(m):
            for i in range(n):
                if grid[j][i] != '#':
                    self.check(grid, j, i, m, n, grid[j][i])
                    cnt += 1
        return cnt

    def check(self, A, j, i, m, n, previous_color):
        if previous_color != A[j][i]:
            return
        color = A[j][i]
        A[j][i] = '#'
        if 0 <= j - 1 <= m - 1:  # up
            self.check(A, j - 1, i, m, n, color)
        if 0 <= j + 1 <= m - 1:  # down
            self.check(A, j + 1, i, m, n, color)
        if 0 <= i - 1 <= n - 1:  # left
            self.check(A, j, i - 1, m, n, color)
        if 0 <= i + 1 <= n - 1:  # right
            self.check(A, j, i + 1, m, n, color)
