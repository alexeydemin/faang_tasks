from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rotten = deque()
        fresh = 0

        # Initial fill
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        counter = 0
        while len(rotten) and fresh:
            counter += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                # del rotten[0]
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    i = x + dx
                    j = y + dy

                    if i < 0 or i == rows or j < 0 or j == cols or grid[i][j] in [0, 2]:
                        continue
                    grid[i][j] = 2
                    fresh -= 1
                    rotten.append((i, j))

        return counter if fresh == 0 else -1


# print(Solution.orangesRotting(None, grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
# print(Solution.orangesRotting(None, grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
# print(Solution.orangesRotting(None, grid=[[0, 2]]))
# print(Solution.orangesRotting(None, grid=[[2], [1]]))
# print(Solution.orangesRotting(None, grid=[[2, 2, 2, 1, 1]]))
# print(Solution.orangesRotting(None, grid=[[2, 1]]))
print(Solution.orangesRotting(None, grid=[[1, 2]]))

# [2, 2, 2],
# [0, 2, 2],
# [1, 0, 2]
