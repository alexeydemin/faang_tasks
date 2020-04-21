from typing import List


class Solution:
    def numIslands(self, A):
        m = len(A)
        if not m: return 0
        n = len(A[0])
        cnt = 0
        for j in range(m):
            for i in range(n):
                if A[j][i] == 1:
                    self.check(A, j, i, m, n)
                    cnt += 1
        return cnt

    def check(self, A, j, i, m, n):
        if A[j][i] != 1:
            return
        A[j][i] = '#'
        if 0 <= j - 1 <= m - 1:  # up
            self.check(A, j - 1, i, m, n)
        if 0 <= j + 1 <= m - 1:  # down
            self.check(A, j + 1, i, m, n)
        if 0 <= i - 1 <= n - 1:  # left
            self.check(A, j, i - 1, m, n)
        if 0 <= i + 1 <= n - 1:  # right
            self.check(A, j, i + 1, m, n)


s = Solution()
grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]
grid = [[]]
r = s.numIslands(grid)

print(r)
