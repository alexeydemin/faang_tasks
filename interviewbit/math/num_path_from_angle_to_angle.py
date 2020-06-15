import sys
sys.setrecursionlimit(5000)

class Solution:
    A = B = k = 0

    def uniquePaths(self, A, B):
        Solution.A = A - 1
        Solution.B = B - 1
        Solution.k = 0
        Solution.getNum(self, 0, 0)
        return Solution.k

    def getNum(self, x, y):
        if x == Solution.A and y == Solution.B:
            Solution.k += 1
        if x < Solution.A:
            Solution.getNum(self, x + 1, y)
        if y < Solution.B:
            Solution.getNum(self, x, y + 1)


def num_path(m, n):  # m,n - ints
  start = 0, 0
  finish = m - 1, n - 1
  pathes = [finish]  # (x, y)
  while pathes[0] != (0, 0):
    new_pathes = []
    for x, y in pathes:
       if x > 0:
         new_pathes.append((x - 1, y))
       if y > 0:
         new_pathes.append((x, y - 1))
    pathes = new_pathes
  #
  return len(pathes)


def count_paths(m, n):
    # corner cases e.g. m=n=0

    dp = [[1 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m - 1]


def num_path(m, n):  # m,n - ints
    dp = [1 for _ in range(m)]
    prev = 1
    for i in range(1, n):
        tmp = []
        for j in range(1, m):
            cur = tmp[j - 1] + dp[j]
            tmp.append(cur)
            dp = tmp

    return dp[m - 1]

def uniquePaths2(m: int, n: int) -> int:
    paths = [1]*n #O(n)
    for i in range(1, m):
        for j in range(1, n):
            paths[j] += paths[j-1] # O(m*n)
    return paths[n-1]


#r = Solution.uniquePaths(None, 2, 3)
r = uniquePaths2(7, 3)
print(r)
