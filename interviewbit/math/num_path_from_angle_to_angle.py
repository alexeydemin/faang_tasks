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


r = Solution.uniquePaths(None, 1, 3000)
print(r)
