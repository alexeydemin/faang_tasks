from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0:
            return -1
        # visited = []
        q = deque([(0, 0, 1)])
        dirs = [
            [-1, -1],
            [-1, 0],
            [-1, 1],

            [0, -1],
            # [0, 0],
            [0, 1],

            [1, -1],
            [1, 0],
            [1, 1],
        ]

        while q:
            x, y, cnt = q.popleft()

            if x == n - 1 == y:
                return cnt

            for [i, j] in dirs:
                if 0 <= x + i < n and 0 <= y + j < n and grid[x + i][y + j] == 0 and (x + i, y + i):
                    # visited.add((x + i, y + j))
                    grid[x + i][y + j] == 2
                    q.append((x + i, y + j, cnt + 1))

        return -1


print(Solution.shortestPathBinaryMatrix(None, grid=[
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]))  # 4

print(Solution.shortestPathBinaryMatrix(None, grid=[
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))  # 4

print(Solution.shortestPathBinaryMatrix(None, grid=[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]))  # 3

print(Solution.shortestPathBinaryMatrix(None, grid=[
    [0, 1],
    [1, 0]
]))  # 2
