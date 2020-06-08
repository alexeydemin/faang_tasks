class Solution:
    def maximalSquare(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows else 0
        dp = [0 for _ in range(cols+1)]
        mx = prev = 0
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                temp = dp[j]
                if int(matrix[i-1][j-1]):
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                    mx = max(mx, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return mx * mx


print(Solution.maximalSquare(None,

                             [["1"], ["0"], ["1"], ["1"], ["1"], ["1"], ["0"]]


                             ))
