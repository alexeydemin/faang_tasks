from typing import List
from collections import deque


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    q.append((i, j, 0))
                    break
        while q:
            r, c, d = q.popleft()
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + x
                nc = c + y
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] in ['#', 'O']:
                    if grid[nr][nc] == '#':
                        return d + 1
                    grid[nr][nc] = 'V'
                    q.append((nr, nc, d + 1))
        return -1

    # '*' is your location. There is exactly one '*' cell.
    # '#' is a food cell. There may be multiple food cells.
    # 'O' is free space, and you can travel through these cells.
    # 'X' is an obstacle, and you cannot travel through these cells.
    # * ---> 0 ---> #


grid = [
    ["X", "X", "X", "X", "X", "X"],
    ["X", "*", "O", "O", "O", "X"],
    ["X", "O", "O", "#", "O", "X"]
]
print(Solution.getFood(None, grid))
