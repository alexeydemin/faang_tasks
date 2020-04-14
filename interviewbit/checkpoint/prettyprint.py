import numpy as np


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        len = A * 2 - 1
        arr = [[0] * len for _ in range(len)]
        for m in range(len):
            for i in range(len):
                for j in range(len):
                    if ((i == m or i == len - m - 1) and m <= j <= len - 1 - m) or ((j == m or j == len - m - 1) and m <= i <= len - 1 - m):
                        arr[i][j] = str(A - m)
        return arr


r = Solution.prettyPrint(None, 4)
print(np.matrix(r))
