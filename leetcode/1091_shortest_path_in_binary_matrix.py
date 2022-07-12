from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def dfs(i, j, cnt, grid):
            n = len(grid)
            if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                if i == j == n - 1:
                    return cnt + 1
                grid[i][j] = 8
                dfs(i + 1, j, cnt + 1, grid)
                dfs(i + 1, j + 1, cnt + 1, grid)
                dfs(i, j + 1, cnt + 1, grid)
                dfs(i - 1, j + 1, cnt + 1, grid)

                dfs(i - 1, j, cnt + 1, grid)
                dfs(i - 1, j - 1, cnt + 1, grid)
                dfs(i, j - 1, cnt + 1, grid)
                dfs(i + 1, j - 1, cnt + 1, grid)

        if len(grid) == 1:
            return 0
        return dfs(0, 0, 0, grid) or -1


print(Solution.shortestPathBinaryMatrix(None, grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]]))
