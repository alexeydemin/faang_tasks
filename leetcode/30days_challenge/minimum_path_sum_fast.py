from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])

        for j in range(1, m):
            grid[j][0] += grid[j-1][0]

        for i in range(1, n):
            grid[0][i] += grid[0][i-1]

        for j in range(1, m):
            for i in range(1, n):
                grid[j][i] += min(grid[j-1][i],grid[j][i-1])

        return grid[m-1][n-1]


s = Solution()
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(s.minPathSum(grid))  # 7