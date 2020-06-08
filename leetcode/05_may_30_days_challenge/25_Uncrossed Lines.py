from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for i in range(len(A))] for j in range(len(B))]
        #return dp
        for i in range(len(B)):
            for j in range(len(A)):
                if j and i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif i and j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i-1][j-1] + int(A[j] == B[i])
                    )

        return dp[len(B) - 1][len(A) - 1]


# print(Solution.maxUncrossedLines(None, A=[1, 4, 2], B=[1, 2, 4]))  # 2
# print(Solution.maxUncrossedLines(None, A=[2, 5, 1, 2, 5], B=[10, 5, 2, 1, 5, 2]))  # 3
# print(Solution.maxUncrossedLines(None, A=[1, 3, 7, 1, 7, 5], B=[1, 9, 2, 5, 1]))  # 2
print(Solution.maxUncrossedLines(None, [2,1], [1,2,1,3,3,2]))  # 2
